from unittest.mock import patch
from infrastructure.FMP_client import FMPclient
import json
import os

def test_FMPclient_create():
    key = "Fake-API-key"
    API = FMPclient(key)
    assert API.api_key == key 

@patch("infrastructure.FMP_client.requests.get")
def test_get_current_price(mock_get):
    ressource_path = os.path.join(".", "ressource", "responseQuoteBySymbol.json")

    with open(ressource_path, 'r') as f:
        mock_json = json.load(f)

    mock_response = mock_get
    mock_response.status_code = 200
    mock_response.json.return_value = mock_json

    client = FMPclient("FakeKey")
    price = client.get_current_price("AAPL")

    assert price == 145.775
    mock_get.assert_called_once()
    