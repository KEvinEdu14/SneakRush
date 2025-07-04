import os, secrets, datetime as dt
from sqlalchemy.orm import Session
from infrastructure.db.sqlalchemy import SessionLocal
from domain.entities.reset_token import ResetToken
from infrastructure.notifications.send_notification import send_mail

EXP_MINUTES = int(os.getenv("RESET_TOKEN_EXP_MINUTES", 15))

def execute(email: str) -> dict:
    token   = secrets.token_urlsafe(32)
    expires = dt.datetime.utcnow() + dt.timedelta(minutes=EXP_MINUTES)

    db: Session = SessionLocal()
    db_token = ResetToken(token=token, email=email, expires_at=expires)
    db.add(db_token)
    db.commit()

    reset_link = f"https://frontend/reset-password?token={token}"
    send_mail(email, f"Reset your password using this link: {reset_link}")
    return {"sent": True}
