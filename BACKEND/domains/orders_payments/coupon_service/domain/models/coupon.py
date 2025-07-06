from sqlalchemy import Column, String, Float, Boolean
from config.db import Base

class Coupon(Base):
    __tablename__ = 'coupons'
    code = Column(String(50), primary_key=True, unique=True, index=True)
    discount = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
