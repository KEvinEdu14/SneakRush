import os, httpx

class StockClient:
    BASE_URL = os.getenv("STOCK_SERVICE_URL")

    @classmethod
    async def check_stock(cls, product_id: str, quantity: int):
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{cls.BASE_URL}/stock/{product_id}")
            resp.raise_for_status()
            data = resp.json()
            return data.get('available', 0) >= quantity
