from domain.models import Asset, UnknownSymbol
from domain.portfolio_repository import PortfolioRepository
from infrastructure.market_data_provider import MarketDataProvider

class AddAssetToPortfolio:
    def __init__(self, repo: PortfolioRepository, provider: MarketDataProvider):
        self.repo = repo
        self.provider = provider

    def execute_add_asset(self, asset: Asset):
        try:
            self.provider.get_current_price(asset.symbol)
        except UnknownSymbol:
            raise ValueError(f"Unknown symbol: {asset.symbol}")
        
        self.repo.save(asset)
