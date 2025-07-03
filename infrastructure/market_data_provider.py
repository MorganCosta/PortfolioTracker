from abc import ABC, abstractmethod

class MarketDataProvider(ABC):
    @abstractmethod
    def get_current_price(self, symbol):
        """return float value from a symbol asset (as stock, etf...) """
        pass