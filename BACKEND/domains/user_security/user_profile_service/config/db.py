
# config/db.py

import os
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# ✅ Se obtiene la URL desde la variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# ✅ Motor de base de datos asincrónico (requiere asyncpg)
engine = create_async_engine(
    DATABASE_URL,
    echo=True,          # opcional: imprime queries en consola
    future=True
)

# ✅ Sesiones asincrónicas con SQLAlchemy
async_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)
