from domain.models import Asset, Portfolio

def test_asset_create():
    stock = Asset(symbol="COKE", price_bought=50.0, qty=10)
    assert stock.symbol == "COKE"
    assert stock.price_bought == 50
    assert stock.qty == 10

def test_portfolio_create():
    stock1 = Asset(symbol="TTE.PA", price_bought=54.107, qty=14)
    etf1 = Asset(symbol="WPEA.PA", price_bought=5.686, qty=263)
    french_PEA = Portfolio(assets=[stock1, etf1])
    assert len(french_PEA.assets) == 2
    assert french_PEA.assets[0].symbol == "TTE.PA"
    assert french_PEA.assets[0].price_bought == 54.107
    assert french_PEA.assets[0].qty == 14

    assert french_PEA.assets[1].symbol == "WPEA.PA"
    assert french_PEA.assets[1].price_bought == 5.686
    assert french_PEA.assets[1].qty == 263
    