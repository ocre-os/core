from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.core.database import Base, get_db
from app.main import app


def client():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    Base.metadata.create_all(engine)
    def override_db():
        with Session(engine, expire_on_commit=False) as session:
            yield session
    app.dependency_overrides[get_db] = override_db
    return TestClient(app), engine


def test_bootstrap_login_and_protected_organization():
    test_client, engine = client()
    try:
        response = test_client.get("/api/v1/organizaciones")
        assert response.status_code == 401
        response = test_client.post("/api/v1/auth/register", json={"email": "Admin@Example.com", "password": "correct horse battery", "nombre_mostrado": "Admin"})
        assert response.status_code == 201
        assert "password_hash" not in response.text
        assert test_client.post("/api/v1/auth/register", json={"email": "other@example.com", "password": "correct horse battery", "nombre_mostrado": "Other"}).status_code == 409
        assert test_client.post("/api/v1/auth/login", json={"email": "admin@example.com", "password": "wrong password"}).status_code == 401
        token = test_client.post("/api/v1/auth/login", json={"email": "admin@example.com", "password": "correct horse battery"}).json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        assert test_client.get("/api/v1/auth/me", headers=headers).status_code == 200
        created = test_client.post("/api/v1/organizaciones", headers=headers, json={"nombre_comercial": "Ocre"})
        assert created.status_code == 201
        assert created.json().get("created_by", True)
        assert test_client.get("/api/v1/organizaciones", headers=headers).status_code == 200
        assert test_client.get("/api/v1/organizaciones", headers={"Authorization": "Bearer invalid"}).status_code == 401
    finally:
        app.dependency_overrides.clear()
        engine.dispose()
