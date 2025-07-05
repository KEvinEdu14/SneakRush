from sqlalchemy.orm import Session
from domain.models.user import User
from interfaces.schemas.user_schema import UserCreate, UserUpdate

def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id, User.is_active == True).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).filter(User.is_active == True).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate):
    db_user = User(email=user.email, first_name=user.first_name, last_name=user.last_name, avatar_url=user.avatar_url)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: str, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    for var, value in vars(user).items():
        if value is not None:
            setattr(db_user, var, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: str):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    db_user.is_active = False
    db.commit()
    db.refresh(db_user)
    return db_user
