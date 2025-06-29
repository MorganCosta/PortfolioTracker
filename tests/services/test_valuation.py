import pytest
from services.valuation import calculate_profit

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

