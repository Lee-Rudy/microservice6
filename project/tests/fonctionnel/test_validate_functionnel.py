from fastapi.testclient import TestClient

from project.main import app


client = TestClient(app)


def test_normal():
    r = client.post("/validate", json={"sensor": "co2", "value": 500.0})
    assert r.status_code == 200
    payload = r.json()
    assert payload["valid"] is True
    assert payload["level"] == "normal"
    assert payload["sensor"] == "co2"
    assert payload["threshold"] == 800.0
    assert isinstance(payload["timestamp"], str) and payload["timestamp"].endswith("Z")


def test_moderate():
    r = client.post("/validate", json={"sensor": "co2", "value": 850.0})
    assert r.status_code == 200
    payload = r.json()
    assert payload["valid"] is True
    assert payload["level"] == "moderate"
    assert payload["sensor"] == "co2"
    assert payload["threshold"] == 800.0


def test_critical():
    r = client.post("/validate", json={"sensor": "co2", "value": 1500.0})
    assert r.status_code == 200
    payload = r.json()
    assert payload["valid"] is False
    assert payload["level"] == "critical"
    assert payload["sensor"] == "co2"
    assert payload["threshold"] == 1000.0


def test_inconnu():
    r = client.post("/validate", json={"sensor": "inconnu", "value": 10.0})
    assert r.status_code == 200
    payload = r.json()
    assert payload["valid"] is False
    assert payload["level"] == "unknown"
    assert payload["message"] == "Capteur non répertorié"
