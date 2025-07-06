from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.db import SessionLocal, engine, Base
from interfaces.controllers.coupon_controller import validate_coupon_controller
from interfaces.schemas.coupon_schema import CouponValidateResponse

# Create tables
Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/coupons", tags=["coupons"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{code}/validate", response_model=CouponValidateResponse)
async def validate_coupon(code: str, db: Session = Depends(get_db)):
    return await validate_coupon_controller(db, code)
