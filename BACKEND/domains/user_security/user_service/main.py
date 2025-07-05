from fastapi import FastAPI
from interfaces.routes.user_routes import router as user_router

app = FastAPI(
    title="User Service",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs"
)

app.include_router(user_router)
