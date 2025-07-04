from fastapi import FastAPI
from interfaces.routes import router

app = FastAPI()

# Esto es clave: incluir el router bajo el prefijo correcto
app.include_router(router, prefix="/api/profile")
