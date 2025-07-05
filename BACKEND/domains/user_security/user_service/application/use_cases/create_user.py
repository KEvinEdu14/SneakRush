from infrastructure.repositories.user_repo import create_user as repo_create_user
from sqlalchemy.orm import Session
from interfaces.schemas.user_schema import UserCreate

def create_user(db: Session, user: UserCreate):
    return repo_create_user(db, user)
