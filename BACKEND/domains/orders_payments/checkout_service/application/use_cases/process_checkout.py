from sqlalchemy.orm import Session
from infrastructure.repositories.checkout_repo import create_order
from interfaces.clients.cart_client import CartClient
from interfaces.clients.stock_client import StockClient
from interfaces.clients.coupon_client import CouponClient

async def process_checkout(db: Session, user_id: str, coupon_code: str = None):
    items = await CartClient.get_items(user_id)
    if not items:
        raise ValueError("Cart is empty")
    for item in items:
        if not await StockClient.check_stock(item['productId'], item['quantity']):
            raise ValueError(f"Insufficient stock for product {item['productId']}")
    discount = 0.0
    if coupon_code:
        discount = await CouponClient.validate_coupon(coupon_code)
    total = sum(item['quantity'] * item.get('price', 0) for item in items)
    total *= (1 - discount)
    order = create_order(db, user_id, items, total)
    return order
