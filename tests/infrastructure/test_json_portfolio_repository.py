import os
import json
import pytest
from infrastructure.json_portfolio_repository import JsonPortfolioRepository
from domain.models import Asset

@pytest.fixture
def test_file():
    filename = "my_portfolio.json"
    yield filename
    if os.path.exists(filename):
        os.remove(filename)

def test_add_and_read_assets(test_file):
    repo = JsonPortfolioRepository(test_file)
    stock = Asset("AAPL", 100.00, 10)
    repo.save(stock)
    my_portfolio = repo.get()
    assert len(my_portfolio) == 1
    assert my_portfolio[0].symbol == "AAPL"
