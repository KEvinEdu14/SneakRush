from datetime import date
from pydantic import BaseModel, EmailStr
from typing import Optional

class ProfileCreate(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    bio: Optional[str] = None
    image_url: Optional[str] = None
    birthdate: Optional[date] = None


class ProfileUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None

class ProfileOut(BaseModel):
    id: int
    email: EmailStr
    full_name: Optional[str]
    phone: Optional[str]

    class Config:
        orm_mode = True
