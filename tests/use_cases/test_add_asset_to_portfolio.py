import pytest
from domain.models import Asset
from use_cases.add_asset_to_portfolio import AddAssetToPortfolio

class DummyRepo:
    def __init__(self):
        self.assets = []

    def add(self, asset):
        self.assets.append(asset)

    def get(self):
        return self.assets

class DummyProvider:
    def get_current_price(self, symbol):
        return 100.0

def test_add_asset_adds_asset_to_repo():
    repo = DummyRepo()
    provider = DummyProvider()
    use_case = AddAssetToPortfolio(repo, provider)

    asset = Asset("AAPL", 200.00, 10)
    use_case.execute_add_asset(asset)

    assets = repo.get()
    assert len(assets) == 1
    assert assets[0].symbol == "AAPL"
    assert assets[0].qty == 10
