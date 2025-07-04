from passlib.hash import bcrypt
from sqlalchemy.orm import Session
from infrastructure.db.sqlalchemy import SessionLocal
from domain.entities.reset_token import ResetToken
from infrastructure.db.models.user_model import User

def execute(token: str, new_password: str) -> dict:
    db: Session = SessionLocal()

    rt: ResetToken | None = db.query(ResetToken).filter_by(token=token).first()
    if not rt or rt.expired:
        return {"ok": False, "reason": "invalid_or_expired"}

    user = db.query(User).filter_by(email=rt.email).first()
    if not user:
        return {"ok": False, "reason": "user_not_found"}

    user.password = bcrypt.hash(new_password)
    db.delete(rt)
    db.commit()
    return {"ok": True}
