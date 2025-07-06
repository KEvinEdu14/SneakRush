import os, httpx

class CouponClient:
    BASE_URL = os.getenv("COUPON_SERVICE_URL")

    @classmethod
    async def validate_coupon(cls, code: str):
        async with httpx.AsyncClient() as client:
            resp = await client.get(f"{cls.BASE_URL}/coupons/{code}/validate")
            resp.raise_for_status()
            return resp.json().get('discount', 0.0)
