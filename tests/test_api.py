from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "API em funcionamento"}

def test_get_fotos():
    response = client.get("/fotos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 10