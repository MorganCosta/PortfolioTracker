import pytest
from fastapi.testclient import TestClient
from api.main import app


client = TestClient(app)

def test_add_asset():

    data = {"symbol": "AAPL", "qty": 10, "price": 100}

    response = client.post("/assets", json=data)

    assert response.status_code == 200
    
    json_resp = response.json()
    assert json_resp["message"] == "Asset added"
    assert json_resp["symbol"] == "AAPL"
    assert json_resp["qty"] == 10
