class CalculatePortfolio:
    def __init__(self, repository, market_data_provider):
        self.repository = repository
        self.market_data_provider = market_data_provider
    
    def execute_cal(self):
        assets = self.repository.get()
        total = 0.0

        for asset in assets:
            price = self.market_data_provider.get_current_price(asset.symbol)
            total += price * asset.qty

        return total