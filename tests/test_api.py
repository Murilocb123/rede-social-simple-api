from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "API em funcionamento"}

def test_feed_fotos():
    response = client.get("/feed_fotos")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 10
    assert "id_postagem" in data[0]
