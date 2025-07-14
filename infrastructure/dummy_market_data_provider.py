from infrastructure.market_data_provider import MarketDataProvider

class DummyMarketDataProvider(MarketDataProvider):
    def __init__(self):
        self.prices = {
            "AAPL": 150.0,
            "COKE": 50.0,
        }

    def get_current_price(self, symbol: str) -> float:
        if symbol in self.prices:
            return self.prices[symbol]
        else:
            raise ValueError(f"Unknown symbol: {symbol}")
