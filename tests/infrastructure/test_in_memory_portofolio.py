from infrastructure.in_memory_portfololio_repository import InMemoryPortfolioRepository 
from domain.models import Asset

def test_save_and_read_assets():
    repo = InMemoryPortfolioRepository()
    stock = Asset("AAPL", 100.00, 10)
    repo.save(stock)

    view = repo.get()
    
    assert len(view) == 1
    assert view[0].symbol == "AAPL"





