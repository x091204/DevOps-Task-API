import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"DevOps-Task-API" in response.data


def test_add_task(client):
    response = client.post("/add", data={"task": "Test Task"}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Test Task" in response.data


def test_toggle_task(client):
    client.post("/add", data={"task": "Toggle Task"}, follow_redirects=True)
    response = client.get("/toggle/0", follow_redirects=True)
    assert response.status_code == 200


def test_delete_task(client):
    client.post("/add", data={"task": "Delete Task"}, follow_redirects=True)
    response = client.get("/delete/0", follow_redirects=True)
    assert response.status_code == 200