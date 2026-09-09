from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.core.database import Base, get_db
from app.main import app


def test_equipment_relationships_and_temporal_validation():
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
        organization = client.post("/api/v1/organizaciones", headers=headers, json={"nombre_comercial": "Cliente"}).json()
        location = client.post("/api/v1/ubicaciones", headers=headers, json={"organizacion_id": organization["id"], "nombre": "Planta"}).json()
        invalid = {"codigo": "EQ-1", "fecha_alta": "2026-01-02T00:00:00Z"}
        assert client.post("/api/v1/equipos", headers=headers, json=invalid).status_code == 201
        duplicate = client.post("/api/v1/equipos", headers=headers, json=invalid)
        assert duplicate.status_code == 409
        equipo = client.get("/api/v1/equipos", headers=headers).json()[0]
        assert client.post(f"/api/v1/equipos/{equipo['id']}/organizaciones", headers=headers, json={"organizacion_id": organization["id"], "tipo_relacion": "responsable", "desde": "2026-01-01T00:00:00Z", "hasta": "2025-01-01T00:00:00Z"}).status_code == 422
        relation = client.post(f"/api/v1/equipos/{equipo['id']}/ubicaciones", headers=headers, json={"ubicacion_id": location["id"], "desde": "2026-01-01T00:00:00Z"})
        assert relation.status_code == 201
        assert client.post(f"/api/v1/equipos/{equipo['id']}/ubicaciones", headers=headers, json={"ubicacion_id": location["id"], "desde": "2026-02-01T00:00:00Z"}).status_code == 409
    finally:
        app.dependency_overrides.clear()
        engine.dispose()
