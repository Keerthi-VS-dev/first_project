from sqlalchemy import Column, BigInteger, String, Boolean, Enum, DateTime
from app.database import Base


class User(Base):
    __tablename__ = "users"


    id = Column(BigInteger, primary_key=True, index=True)
    email = Column(String(100), unique=True)
    password_hashed = Column(String(255))
    role = Column(Enum('ADMIN','EMPLOYEE'))
    is_active = Column(Boolean, default=True)
    last_login = Column(DateTime)
    created_at = Column(DateTime(timezone=True), server_default=func.now())