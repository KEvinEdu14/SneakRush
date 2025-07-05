import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://"), pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def init_db():
    # importa modelos para que Base los conozca
    from domain.entities.reset_token import ResetToken
    from infrastructure.db.models.user_model import User
    Base.metadata.create_all(bind=engine)
