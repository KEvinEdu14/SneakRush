from sqlalchemy.orm import Session
from application.use_cases.create_user import create_user as uc_create_user
from application.use_cases.get_user import get_user as uc_get_user
from application.use_cases.get_users import get_users as uc_get_users
from application.use_cases.update_user import update_user as uc_update_user
from application.use_cases.delete_user import delete_user as uc_delete_user
from interfaces.schemas.user_schema import UserCreate, UserUpdate
from interfaces.clients.external_clients import notify_profile_created, notify_profile_updated

async def create_user_controller(db: Session, user: UserCreate):
    new_user = uc_create_user(db, user)
    await notify_profile_created(str(new_user.id))
    return new_user

def get_user_controller(db: Session, user_id: str):
    return uc_get_user(db, user_id)

def get_users_controller(db: Session, skip: int, limit: int):
    return uc_get_users(db, skip, limit)

async def update_user_controller(db: Session, user_id: str, user: UserUpdate):
    updated = uc_update_user(db, user_id, user)
    if updated:
        await notify_profile_updated(str(updated.id))
    return updated

def delete_user_controller(db: Session, user_id: str):
    return uc_delete_user(db, user_id)
