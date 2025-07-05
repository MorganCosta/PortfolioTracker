from domain.models import Asset
from infrastructure.market_data_provider import MarketDataProvider

def calculate_profit(price_bought: float, price_current: float, qty: float) -> float:
    return (price_current - price_bought) * qty

class ValuationService:
    def __init__(self, maket_data_provider : MarketDataProvider):
        self.maket_data_provider = maket_data_provider

    def calculate_profit(self, asset : Asset) -> float:
        current_price = self.maket_data_provider.get_current_price(asset.symbol)
        return (current_price - asset.price_bought) * asset.qty
