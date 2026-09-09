from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.core.database import Base, get_db
from app.main import app


def test_locations_require_existing_organization():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    Base.metadata.create_all(engine)

    def override_db():
        with Session(engine, expire_on_commit=False) as session:
            yield session

    app.dependency_overrides[get_db] = override_db
    client = TestClient(app)
    try:
        client.post("/api/v1/auth/register", json={"email": "admin@example.com", "password": "correct horse battery", "nombre_mostrado": "Admin"})
        token = client.post("/api/v1/auth/login", json={"email": "admin@example.com", "password": "correct horse battery"}).json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        missing = "00000000-0000-0000-0000-000000000000"
        assert client.post("/api/v1/ubicaciones", headers=headers, json={"organizacion_id": missing, "nombre": "Planta"}).status_code == 404
        organization = client.post("/api/v1/organizaciones", headers=headers, json={"nombre_comercial": "Cliente"}).json()
        created = client.post("/api/v1/ubicaciones", headers=headers, json={"organizacion_id": organization["id"], "nombre": "Planta", "pais": "MX"})
        assert created.status_code == 201
        location_id = created.json()["id"]
        assert client.get(f"/api/v1/ubicaciones/{location_id}", headers=headers).status_code == 200
        assert len(client.get(f"/api/v1/ubicaciones?organizacion_id={organization['id']}", headers=headers).json()) == 1
    finally:
        app.dependency_overrides.clear()
        engine.dispose()
