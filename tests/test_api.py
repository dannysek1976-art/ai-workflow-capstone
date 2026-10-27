from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_predict():
    response = client.post("/predict", json={"country": "Italia", "feature_1": 10.0})
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] == 20.0
