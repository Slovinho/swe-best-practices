from fastapi.testclient import TestClient

from app.main import app


def test_health_when_database_url_is_missing(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    response = TestClient(app).get("/health")
    assert response.status_code == 503
    assert response.json() == {
        "status": "degraded",
        "database": "missing_config",
    }
