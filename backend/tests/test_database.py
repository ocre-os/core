"""Opt-in PostgreSQL checks; each test creates and drops its own temporary database."""

import os
import subprocess
import sys
from contextlib import contextmanager
from datetime import UTC, datetime
from pathlib import Path
from uuid import UUID, uuid4

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, inspect
from sqlalchemy.engine import make_url
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.database import get_db
from app.core.security import create_access_token, hash_password
from app.main import app
from app.modules.identity.models import Usuario
from app.modules.organizations.models import Organizacion

pytestmark = pytest.mark.skipif(
    os.environ.get("OCRE_RUN_DB_TESTS") != "1",
    reason="Set OCRE_RUN_DB_TESTS=1 against the local development PostgreSQL instance",
)


def migrate(url: str, *args: str) -> None:
    result = subprocess.run(
        [sys.executable, "-m", "alembic", *args],
        cwd=Path(__file__).resolve().parents[1],
        env={**os.environ, "DATABASE_URL": url},
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


@pytest.fixture
def database():
    name = "ocre_test_" + uuid4().hex
    source = make_url(get_settings().database_url)
    admin = create_engine(source.set(database="postgres"), isolation_level="AUTOCOMMIT")
    url = source.set(database=name).render_as_string(hide_password=False)
    engine = create_engine(url)
    try:
        with admin.connect() as connection:
            connection.exec_driver_sql(f'CREATE DATABASE "{name}"')
        try:
            migrate(url, "upgrade", "head")
            yield engine, url
        finally:
            engine.dispose()
            with admin.connect() as connection:
                connection.exec_driver_sql(f'DROP DATABASE "{name}"')
    finally:
        admin.dispose()


def test_migrations_round_trip_and_metadata(database) -> None:
    engine, url = database
    assert len(inspect(engine).get_table_names()) == 13  # 12 domain tables + Alembic
    migrate(url, "check")
    migrate(url, "upgrade", "head")  # Applying the same head is safe.
    migrate(url, "downgrade", "base")
    assert inspect(engine).get_table_names() == ["alembic_version"]
    migrate(url, "upgrade", "head")
    migrate(url, "check")
    for table, column in [("equipo", "codigo"), ("usuario", "email")]:
        assert any(
            index["unique"] and index["column_names"] == [column]
            for index in inspect(engine).get_indexes(table)
        )


@contextmanager
def api_client(engine):
    def override_db():
        with Session(engine, expire_on_commit=False) as session:
            yield session

    previous = app.dependency_overrides.copy()
    app.dependency_overrides[get_db] = override_db
    with Session(engine) as session:
        user = Usuario(email="test@example.com", password_hash=hash_password("test password 123"), nombre_mostrado="Test")
        session.add(user)
        session.commit()
        token = create_access_token(user.id)
    try:
        with TestClient(app) as client:
            client.headers.update({"Authorization": f"Bearer {token}"})
            yield client
    finally:
        app.dependency_overrides.clear()
        app.dependency_overrides.update(previous)


def test_organization_persistence_and_archiving(database) -> None:
    engine, _ = database
    with api_client(engine) as client:
        payload = {
            "nombre_comercial": "Á" * 200,
            "nombre_legal": "L" * 250,
            "telefono_principal": "1" * 40,
            "email_general": "e" * 320,
            "sitio_web": "w" * 500,
            "estado_relacion": "r" * 60,
        }
        response = client.post("/api/v1/organizaciones", json=payload)
        assert response.status_code == 201, response.text
        record = response.json()
        assert all(record[field] == value for field, value in payload.items())
        assert record["created_at"] and record["updated_at"]
        record_id = record["id"]
        path = f"/api/v1/organizaciones/{record_id}"
        assert client.get(path).json() == record
        assert client.get("/api/v1/organizaciones").json() == [record]
        assert client.get("/api/v1/organizaciones?offset=1").json() == []
        assert client.get("/api/v1/organizaciones?limit=0").status_code == 422
        assert client.get(f"/api/v1/organizaciones/{uuid4()}").status_code == 404
        assert client.get("/api/v1/organizaciones/not-a-uuid").status_code == 422

        with Session(engine) as session:
            organization = session.get(Organizacion, UUID(record_id))
            assert organization is not None
            organization.archived_at = datetime.now(UTC)
            session.commit()
        assert client.get(path).status_code == 404
        assert client.get("/api/v1/organizaciones").json() == []
        with Session(engine) as session:
            assert session.get(Organizacion, UUID(record_id)) is not None
