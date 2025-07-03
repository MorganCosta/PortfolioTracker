from infrastructure.market_data_provider import MarketDataProvider

class DummyMarketDataProvider(MarketDataProvider):
    def get_current_price(sefl, symbol): 
        return 50.50

def test_dummy_market_data_provider():
    provider = DummyMarketDataProvider()
    price = provider.get_current_price("COKE")
    assert price == 50.50
