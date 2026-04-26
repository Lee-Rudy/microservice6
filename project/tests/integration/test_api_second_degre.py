from fastapi.testclient import TestClient

from project.main import app


client = TestClient(app)


def test_post_calculer_returns_expected_solution():
    response = client.post("/degre/calculer", json={"a": 1, "b": -3, "c": 2})

    assert response.status_code == 200
    payload = response.json()
    assert payload["discriminant"] == 1.0
    assert payload["solutions"] == [1.0, 2.0]
    assert payload["has_real_solutions"] is True


def test_post_calculer_invalid_equation_returns_422():
    response = client.post("/degre/calculer", json={"a": 0, "b": 1, "c": 1})

    assert response.status_code == 422


def test_post_calculer_invalid_payload_returns_422():
    response = client.post("/degre/calculer", json={"a": "invalid", "b": 1, "c": 1})

    assert response.status_code == 422


def test_root_endpoint_returns_ms6():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"status": "ms6"}


def test_post_calculer_returns_no_real_solutions():
    response = client.post("/degre/calculer", json={"a": 1, "b": 0, "c": 1})

    assert response.status_code == 200
    payload = response.json()
    assert payload["discriminant"] == -4.0
    assert payload["solutions"] == [None, None]
    assert payload["has_real_solutions"] is False


def test_health_endpoint_returns_healthy():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
