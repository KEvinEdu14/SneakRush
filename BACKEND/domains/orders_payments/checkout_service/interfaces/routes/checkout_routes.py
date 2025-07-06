from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from config.db import SessionLocal, engine, Base
from interfaces.controllers.checkout_controller import checkout_controller
from interfaces.schemas.order_schema import CheckoutResponse

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/checkout", tags=["checkout"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{user_id}", response_model=CheckoutResponse)
async def checkout(user_id: str, coupon: str = Query(None), db: Session = Depends(get_db)):
    return await checkout_controller(db, user_id, coupon)
