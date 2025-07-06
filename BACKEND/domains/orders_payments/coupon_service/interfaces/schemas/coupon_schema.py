from pydantic import BaseModel

class CouponValidateResponse(BaseModel):
    code: str
    discount: float
