import os
import httpx

AUTH_SERVICE_URL         = os.getenv("AUTH_SERVICE_URL")
NOTIFICATION_SERVICE_URL = os.getenv("NOTIFICATION_SERVICE_URL")

async def notify_profile_created(user_id: str):
    if NOTIFICATION_SERVICE_URL:
        async with httpx.AsyncClient() as client:
            await client.post(
                NOTIFICATION_SERVICE_URL,
                json={"user_id": user_id, "event": "profile_created"}
            )

async def notify_profile_updated(user_id: str):
    if NOTIFICATION_SERVICE_URL:
        async with httpx.AsyncClient() as client:
            await client.post(
                NOTIFICATION_SERVICE_URL,
                json={"user_id": user_id, "event": "profile_updated"}
            )
