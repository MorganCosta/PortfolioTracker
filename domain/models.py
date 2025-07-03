class Asset:
    def __init__(self, symbol: str, price_bought: float, qty: float):
        self.symbol = symbol
        self.price_bought = price_bought
        self.qty = qty


class Portfolio:
    def __init__(self, assets: Asset ):
        self.assets = assets
        