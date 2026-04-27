from fastapi.testclient import TestClient

from project.main import app


client = TestClient(app)


def test_post_validate_unknown_sensor():
    r = client.post("/validate", json={"sensor": "x", "value": 1.0})
    assert r.status_code == 200
    payload = r.json()
    assert payload["valid"] is False
    assert payload["level"] == "unknown"
    assert payload["message"] == "Capteur non répertorié"


def test_post_validate_invalid_payload_returns_422():
    r = client.post("/validate", json={"sensor": "co2", "value": "bad"})
    assert r.status_code == 422


def test_system_endpoints():
    assert client.get("/").status_code == 200
    assert client.get("/health").status_code == 200
