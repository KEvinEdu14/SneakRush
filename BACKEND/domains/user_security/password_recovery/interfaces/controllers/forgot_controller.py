from fastapi import APIRouter, status
from pydantic import BaseModel, EmailStr
from application.use_cases.create_reset_token import execute

router = APIRouter()

class ForgotIn(BaseModel):
    email: EmailStr

@router.post("/forgot", status_code=status.HTTP_200_OK)
def forgot(body: ForgotIn):
    execute(body.email)
    return {"sent": True}
