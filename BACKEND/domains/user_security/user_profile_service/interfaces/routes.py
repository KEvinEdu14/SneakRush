from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import async_session
from interfaces.schemas import ProfileCreate, ProfileOut, ProfileUpdate
from application.use_cases import profile_use_cases

router = APIRouter()

async def get_session():
    async with async_session() as session:
        yield session

@router.post("", response_model=ProfileOut, status_code=201)
async def create_profile(profile: ProfileCreate, session: AsyncSession = Depends(get_session)):
    return await profile_use_cases.create_profile(session, profile)


@router.get("/{email}", response_model=ProfileOut)
async def get_profile(email: str, session: AsyncSession = Depends(get_session)):
    profile = await profile_use_cases.get_profile(session, email)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.put("/{email}", response_model=ProfileOut)
async def update_profile(email: str, updates: ProfileUpdate, session: AsyncSession = Depends(get_session)):
    profile = await profile_use_cases.update_profile(session, email, updates.dict(exclude_unset=True))
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
