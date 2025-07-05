from infrastructure.repositories.user_repo import update_user as repo_update_user
from sqlalchemy.orm import Session
from interfaces.schemas.user_schema import UserUpdate

def update_user(db: Session, user_id: str, user: UserUpdate):
    return repo_update_user(db, user_id, user)
