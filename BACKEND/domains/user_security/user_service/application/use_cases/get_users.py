from infrastructure.repositories.user_repo import get_users as repo_get_users
from sqlalchemy.orm import Session

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return repo_get_users(db, skip, limit)
