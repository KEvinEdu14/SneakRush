from infrastructure.repositories.user_profile_repo import UserProfileRepository

async def create_profile(session, profile_data):
    repo = UserProfileRepository(session)
    return await repo.create(profile_data)

async def get_profile(session, email):
    repo = UserProfileRepository(session)
    return await repo.get_by_email(email)

async def update_profile(session, email, updates):
    repo = UserProfileRepository(session)
    return await repo.update(email, updates)
