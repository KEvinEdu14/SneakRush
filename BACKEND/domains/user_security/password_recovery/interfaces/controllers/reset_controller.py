from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from application.use_cases.reset_password import execute

router = APIRouter()

class ResetIn(BaseModel):
    token: str
    new_password: str = Field(min_length=6)

@router.post("/reset", status_code=status.HTTP_200_OK)
def reset(body: ResetIn):
    result = execute(body.token, body.new_password)
    if not result["ok"]:
        raise HTTPException(status_code=400, detail=result["reason"])
    return {"updated": True}
