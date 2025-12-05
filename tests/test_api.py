from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_api():
    response = client.post("/replace", json={
    	"text": "aku suka nasi"
    })

    assert response.status_code == 200
    assert "result" in response.json()
