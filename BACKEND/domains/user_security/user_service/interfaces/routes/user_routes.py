from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import SessionLocal, engine, Base
from interfaces.schemas.user_schema import User, UserCreate, UserUpdate
from interfaces.controllers.user_controller import (
    create_user_controller,
    get_user_controller,
    get_users_controller,
    update_user_controller,
    delete_user_controller
)

# Create tables
Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return await create_user_controller(db, user)

@router.get("/", response_model=list[User])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_users_controller(db, skip, limit)

@router.get("/{user_id}", response_model=User)
def read_user(user_id: str, db: Session = Depends(get_db)):
    user = get_user_controller(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: str, user: UserUpdate, db: Session = Depends(get_db)):
    updated = await update_user_controller(db, user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}", response_model=User)
async def delete_user(user_id: str, db: Session = Depends(get_db)):
    deleted = delete_user_controller(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted
