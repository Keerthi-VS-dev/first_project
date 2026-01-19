from sqlalchemy import Column, BigInteger, String, DateTime
from app.database import Base


class Department(Base):
    __tablename__ = "departments"


    id = Column(BigInteger, primary_key=True, index=True)
    department_name = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())