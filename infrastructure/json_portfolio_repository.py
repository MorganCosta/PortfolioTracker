import json
import os
from domain.portfolio_repository import PortfolioRepository
from domain.models import Asset

class JsonPortfolioRepository(PortfolioRepository):
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)

    def get(self):
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        return [Asset(**item) for item in data]
    

    def save(self, asset: Asset):
        assets = self.get()
        assets.append(asset)
        with open(self.file_path, 'w') as f:
            json.dump([a.__dict__ for a in assets], f)
    