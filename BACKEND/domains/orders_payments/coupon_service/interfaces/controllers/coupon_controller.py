from fastapi import HTTPException
from sqlalchemy.orm import Session
from application.use_cases.validate_coupon import validate_coupon
from interfaces.schemas.coupon_schema import CouponValidateResponse

async def validate_coupon_controller(db: Session, code: str):
    discount = validate_coupon(db, code)
    if discount == 0.0:
        raise HTTPException(status_code=404, detail="Coupon not found or inactive")
    return CouponValidateResponse(code=code, discount=discount)
