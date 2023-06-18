from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(settings.DB_URI, pool_pre_ping=True, connect_args={"sslmode": settings.DB_SSLMODE})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
