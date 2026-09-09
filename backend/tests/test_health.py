from fastapi.testclient import TestClient
from sqlalchemy.exc import OperationalError

from app import main
from app.main import app

client = TestClient(app)


def test_health_live() -> None:
    response = client.get("/health/live")

    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert "environment" in payload


def test_readiness_failure_does_not_expose_database_details(monkeypatch) -> None:
    def unavailable():
        raise OperationalError("SELECT 1", {}, Exception("private connection details"))

    monkeypatch.setattr(main.engine, "connect", unavailable)
    response = client.get("/health")
    assert response.status_code == 503
    assert response.json() == {"detail": "database_unavailable"}
    assert client.get("/health/live").status_code == 200
