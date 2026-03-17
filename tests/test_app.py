import pytest
from unittest.mock import patch, MagicMock
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def mock_db():
    with patch('app.get_db') as mock:
        conn = MagicMock()
        cursor = MagicMock()
        cursor.fetchall.return_value = [
            {"id": 1, "task": "Test Task", "done": False, "created_at": "2026-01-01"}
        ]
        cursor.fetchone.return_value = {"id": 1, "task": "Test Task", "done": False}
        conn.cursor.return_value.__enter__ = MagicMock(return_value=cursor)
        conn.cursor.return_value.__exit__ = MagicMock(return_value=False)
        mock.return_value = conn
        yield mock


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"DevOps-Task-API" in response.data


def test_add_task(client):
    response = client.post("/add", data={"task": "Test Task"}, follow_redirects=True)
    assert response.status_code == 200


def test_toggle_task(client):
    response = client.get("/toggle/1", follow_redirects=True)
    assert response.status_code == 200


def test_delete_task(client):
    response = client.get("/delete/1", follow_redirects=True)
    assert response.status_code == 200


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200