from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from domain.models import Asset
from use_cases.add_asset_to_portfolio import AddAssetToPortfolio
from infrastructure.json_portfolio_repository import JsonPortfolioRepository
from infrastructure.dummy_market_data_provider import DummyMarketDataProvider #change to concreat FMP 

app = FastAPI()

@app.get("/health")
def healthcheck():
    return {"status": "ok"}


repo = JsonPortfolioRepository("portfolio.json")
provider = DummyMarketDataProvider() #change later to concreat FMP data
use_case = AddAssetToPortfolio(repo, provider)

class AssetRequest(BaseModel):
    symbol: str
    price: float
    qty: float

@app.post("/assets")
def add_asset(request: AssetRequest):
    try:
        asset = Asset(request.symbol, request.price, request.qty)
        use_case.execute_add_asset(asset)
        return {"message": "Asset added", "symbol": asset.symbol, "qty": asset.qty}
    except Exception as e :
        raise HTTPException(status_code=400, detail=str(e))