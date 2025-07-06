from fastapi import FastAPI
from interfaces.routes.coupon_routes import router as coupon_router

app = FastAPI(
    title="Coupon Service",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs"
)

app.include_router(coupon_router)
