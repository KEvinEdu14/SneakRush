from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    avatar_url: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    avatar_url: Optional[str] = None

class User(UserBase):
    id: UUID
    is_active: bool

    class Config:
        orm_mode = True
