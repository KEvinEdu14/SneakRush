import datetime as dt
from sqlalchemy import Column, String, DateTime
from infrastructure.db.sqlalchemy import Base

class ResetToken(Base):
    __tablename__ = "reset_tokens"

    token      = Column(String, primary_key=True, index=True)
    email      = Column(String, nullable=False, index=True)
    expires_at = Column(DateTime, nullable=False)

    @property
    def expired(self) -> bool:
        return dt.datetime.utcnow() > self.expires_at
