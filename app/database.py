from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
from app.core.config import settings

SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{settings.db_user}:"
    f"{quote_plus(settings.db_password)}@"
    f"{settings.db_host}:{settings.db_port}/"
    f"{settings.db_name}"
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    pool_recycle=1800
)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
