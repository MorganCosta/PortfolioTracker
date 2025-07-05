from infrastructure.FMP_market_data_provider import FMPmarketDataProvider
from infrastructure.FMP_client import FMPclient

class DummyFMPclient:
    def get_current_price(sefl, symbol: str) -> float:
        return 200
    
def test_get_current_price():
    dummy_client = DummyFMPclient()
    provider = FMPmarketDataProvider(dummy_client)
    price = provider.get_current_price("COKE")

    assert price == 200