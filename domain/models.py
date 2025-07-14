class Asset:
    def __init__(self, symbol: str, price_bought: float, qty: float):
        self.symbol = symbol
        self.price_bought = price_bought
        self.qty = qty


class Portfolio:
    def __init__(self, assets: list[Asset] ):
        self.assets = assets
        

class UnknownSymbol(Exception):
    def __init__(self, symbol: str):
        self.symbol = symbol
        super.__init__(f"Unknow symbol: {symbol}")
        