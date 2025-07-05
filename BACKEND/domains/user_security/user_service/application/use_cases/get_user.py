from infrastructure.repositories.user_repo import get_user as repo_get_user
from sqlalchemy.orm import Session

def get_user(db: Session, user_id: str):
    return repo_get_user(db, user_id)
