from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool

from app.core.database import Base, get_db
from app.main import app


def test_contacts_and_organization_link():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    Base.metadata.create_all(engine)

    def override_db():
        with Session(engine, expire_on_commit=False) as session:
            yield session

    app.dependency_overrides[get_db] = override_db
    client = TestClient(app)
    try:
        assert client.get("/api/v1/contactos").status_code == 401
        client.post("/api/v1/auth/register", json={"email": "admin@example.com", "password": "correct horse battery", "nombre_mostrado": "Admin"})
        token = client.post("/api/v1/auth/login", json={"email": "admin@example.com", "password": "correct horse battery"}).json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}
        organization = client.post("/api/v1/organizaciones", headers=headers, json={"nombre_comercial": "Cliente"}).json()
        contact = client.post("/api/v1/contactos", headers=headers, json={"nombre": "Ana", "email_principal": "ana@example.com"})
        assert contact.status_code == 201
        contact_id = contact.json()["id"]
        assert client.get("/api/v1/contactos", headers=headers).json()[0]["nombre"] == "Ana"
        relation = client.post(f"/api/v1/contactos/{contact_id}/organizaciones", headers=headers, json={"organizacion_id": organization["id"], "area": "Compras", "roles": ["compras"], "puede_autorizar": True})
        assert relation.status_code == 201
        assert relation.json()["organizacion_id"] == organization["id"]
        assert client.post(f"/api/v1/contactos/{contact_id}/organizaciones", headers=headers, json={"organizacion_id": organization["id"]}).status_code == 409
    finally:
        app.dependency_overrides.clear()
        engine.dispose()
