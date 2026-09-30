from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["name"] == (
        "AniVora Compute"
    )


def test_health():

    response = client.get(
        "/health"
    )

    assert response.status_code == 200

    assert response.json()["status"] == (
        "healthy"
    )


def test_status():

    response = client.get(
        "/v1/status"
    )

    assert response.status_code == 200


def test_gpu():

    response = client.get(
        "/v1/gpu"
    )

    assert response.status_code == 200

    assert "gpu" in response.json()


def test_create_job():

    response = client.post(
        "/v1/jobs",
        json={
            "type": "compute",
            "command": "test"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True


def test_list_jobs():

    response = client.get(
        "/v1/jobs"
    )

    assert response.status_code == 200

    assert "jobs" in response.json()
