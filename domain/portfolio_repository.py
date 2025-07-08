from abc import ABC, abstractmethod
from typing import List
from domain.models import Asset

class PortfolioRepository(ABC):
    @abstractmethod
    def save(self, asset: Asset) -> None:
        pass

    @abstractmethod
    def get(self) -> List[Asset]:
        pass