from pydantic import BaseModel
from uuid import UUID
from typing import List

class CartItem(BaseModel):
    id: UUID
    userId: UUID
    productId: UUID
    quantity: int

class CheckoutResponse(BaseModel):
    id: UUID
    user_id: UUID
    items: List[CartItem]
    total: float

    class Config:
        orm_mode = True
