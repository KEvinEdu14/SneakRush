# user_profile_repo.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from domain.models.user_profile_model import UserProfile

class UserProfileRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, profile_data: dict) -> UserProfile:
        profile = UserProfile(**profile_data)
        self.session.add(profile)
        await self.session.commit()
        await self.session.refresh(profile)
        return profile

    async def get(self, user_id: int) -> UserProfile | None:
        result = await self.session.execute(
            select(UserProfile).where(UserProfile.user_id == user_id)
        )
        return result.scalar_one_or_none()

    async def update(self, user_id: int, update_data: dict) -> UserProfile | None:
        profile = await self.get(user_id)
        if profile:
            for key, value in update_data.items():
                setattr(profile, key, value)
            await self.session.commit()
            await self.session.refresh(profile)
        return profile
