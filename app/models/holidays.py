from sqlalchemy import Column, BigInteger, String, Date, Boolean, DateTime
from app.database import Base


class Holiday(Base):
    __tablename__ = "holidays"


    id = Column(BigInteger, primary_key=True)
    date = Column(Date)
    day = Column(String(20))
    holiday_name = Column(String(100))
    is_optional = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())