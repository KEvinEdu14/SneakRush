from sqlalchemy import Column, String, Float, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID
import uuid, datetime
from config.db import Base

class Order(Base):
    __tablename__ = 'orders'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    user_id = Column(UUID(as_uuid=True), nullable=False)
    items = Column(Text, nullable=False)  # JSON string
    total = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
