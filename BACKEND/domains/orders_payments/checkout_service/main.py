from fastapi import FastAPI
from interfaces.routes.checkout_routes import router as checkout_router

app = FastAPI(
    title="Checkout Service",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs"
)

app.include_router(checkout_router)
