import os, dotenv, uvicorn
from fastapi import FastAPI
from infrastructure.db.sqlalchemy import init_db
from interfaces.routes import router

# carga variables de entorno
dotenv.load_dotenv()

app = FastAPI(title="password_recovery")
app.include_router(router)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "password_recovery OK"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv("PORT", 4004)))
