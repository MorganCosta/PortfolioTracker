import pytest
from services.valuation import calculate_profit, ValuationService
from domain.models import Asset

def test_calculate_profit_positive():
    pr_bought = 100
    pr_current = 200
    qty = 10

    result = calculate_profit(pr_bought, pr_current, qty)

    assert result == 1000

def test_calculate_profit_negative():
    pr_bought = 100
    pr_current = 10
    qty = 10

    result = calculate_profit(pr_bought, pr_current, qty)

    assert result == -900

class DummyMarketDataProvider:
    def get_current_price(sefl, symbol: str) -> float:
        return 200
    
def test_clalulate_profil():
    provider = DummyMarketDataProvider()
    service = ValuationService(provider)
    stock = Asset("COKE", 100.0, 10)

    result = service.calculate_profit(stock)

    assert result == (200 - 100) * 10
