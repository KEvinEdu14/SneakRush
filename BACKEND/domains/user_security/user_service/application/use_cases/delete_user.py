from infrastructure.repositories.user_repo import delete_user as repo_delete_user
from sqlalchemy.orm import Session

def delete_user(db: Session, user_id: str):
    return repo_delete_user(db, user_id)
