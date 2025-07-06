import os, httpx

class CartClient:
    BASE_URL = os.getenv("CART_SERVICE_URL")

    @classmethod
    async def get_items(cls, user_id: str):
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{cls.BASE_URL}/cart/{user_id}/items")
            resp.raise_for_status()
            return resp.json()
