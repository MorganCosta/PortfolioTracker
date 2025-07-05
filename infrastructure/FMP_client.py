import requests

class FMPclient:
    BASE_STABLE_URL = "https://financialmodelingprep.com/stable"
    BASE_VERSION_URL = "https://financialmodelingprep.com/api/v3/"

    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_current_price(self, symbol: str) -> float:
        url = f"{self.BASE_VERSION_URL}quote/{symbol}?apikey={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        print(f"DEBUG data: {data}")

        if not data or "price" not in data[0]:
            raise ValueError(f"{symbol} as not be find or are no price")
        
        return data[0]["price"]



    

