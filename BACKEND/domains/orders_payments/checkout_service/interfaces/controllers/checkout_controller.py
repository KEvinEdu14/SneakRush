from fastapi import HTTPException
from application.use_cases.process_checkout import process_checkout
from sqlalchemy.orm import Session

async def checkout_controller(db: Session, user_id: str, coupon_code: str = None):
    try:
        order = await process_checkout(db, user_id, coupon_code)
        return order
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
