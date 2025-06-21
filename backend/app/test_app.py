# backend/app/test_app.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "message": "Backend is running successfully"
    }

def test_message():
    response = client.get("/api/message")
    assert response.status_code == 200
    assert "message" in response.json()
