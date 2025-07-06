from infrastructure.repositories.coupon_repo import get_coupon
from sqlalchemy.orm import Session

def validate_coupon(db: Session, code: str):
    coupon = get_coupon(db, code)
    if not coupon:
        return 0.0
    return coupon.discount
