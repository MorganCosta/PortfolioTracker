import os
import json
from unittest.mock import patch
from infrastructure.FMP_client import FMPclient

def test_FMPclient_create():
    key = "Fake-API-key"
    API = FMPclient(key)
    assert API.api_key == key 

@patch("infrastructure.FMP_client.requests.get")
def test_get_current_price(mock_get):
    mock_response = mock_get.return_value
    mock_response.status_code = 200

    ressource_path = os.path.join(".", "ressource", "responseQuoteBySymbol.json")
    with open(ressource_path, 'r') as f:
        mock_response.json.return_value = json.load(f)
   
    client = FMPclient("FakeAPI-KEY")
    price = client.get_current_price("AAPL")

    assert price == 145.775
    #mock_get.assert_called_once()
    