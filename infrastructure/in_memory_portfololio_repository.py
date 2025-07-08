from domain.portfolio_repository import PortfolioRepository
from domain.models import Asset
from typing import List

class InMemoryPortfolioRepository(PortfolioRepository):
    def __init__(self):
        self._assets = []

    def save(self, asset: Asset) -> None:
        self._assets.append(asset)

    def get(self) -> List[Asset]:
        return self._assets

