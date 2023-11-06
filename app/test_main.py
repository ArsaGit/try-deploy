from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"text": "HI"}


def test_read_info():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == {"info": "testing deployment"}
