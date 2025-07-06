from sqlalchemy.orm import Session
from domain.models.coupon import Coupon

def get_coupon(db: Session, code: str):
    return db.query(Coupon).filter(Coupon.code == code, Coupon.is_active == True).first()
