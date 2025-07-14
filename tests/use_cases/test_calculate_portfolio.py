import pytest
from domain.models import Asset, UnknownSymbol
from use_cases.calculate_portfolio import CalculatePortfolio

class DummyMarketDataProvider:
    def __init__(self):
        self.assets = {
            "AAPL": 200.0,
            "COKE": 50.0
        }

    def get_current_price(self, symbol: str) -> float:
        if symbol not in self.assets:
            raise UnknownSymbol(symbol)
        return self.assets[symbol]
    
class DummyPortfolioRepository:
    def __init__(self):
        self.assets = [
            Asset("AAPL",150, 10),
            Asset("COKE", 45, 5)
        ]
    
    def get(self):
        return self.assets

def test_calculate_portfolio():
    provider = DummyMarketDataProvider()
    repo = DummyPortfolioRepository()

    use_case_positif = CalculatePortfolio(repo, provider)
    total = use_case_positif.execute_cal()
    
    assert total == (10 * 200.0) + (5 * 50.0)
