from sqlalchemy.orm import Session
from domain.models.order import Order
import json

def create_order(db: Session, user_id: str, items: list, total: float):
    order = Order(user_id=user_id, items=json.dumps(items), total=total)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
