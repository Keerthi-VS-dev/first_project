from sqlalchemy import Column, BigInteger, Date, DateTime, DECIMAL, Enum, ForeignKey
from app.database import Base


class Attendance(Base):
    __tablename__ = "attendance"


    id = Column(BigInteger, primary_key=True, index=True)
    employee_id = Column(BigInteger, ForeignKey("employees.id"))
    date = Column(Date)
    check_in_time = Column(DateTime)
    check_out_time = Column(DateTime)
    worked_hours = Column(DECIMAL(5,2))
    status = Column(Enum('PRESENT','ABSENT','HALF_DAY'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())