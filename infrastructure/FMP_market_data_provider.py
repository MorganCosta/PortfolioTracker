from infrastructure.market_data_provider import MarketDataProvider

class FMPmarketDataProvider(MarketDataProvider):
    def __init__(self, FMP_client):
        self.FMP_client = FMP_client

    def get_current_price(self, symbol: str) -> float:
        return self.FMP_client.get_current_price(symbol)