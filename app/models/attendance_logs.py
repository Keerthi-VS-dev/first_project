from sqlalchemy import Column, BigInteger, Enum, DateTime, ForeignKey
from app.database import Base


class AttendanceLog(Base):
    __tablename__ = "attendance_logs"


    id = Column(BigInteger, primary_key=True)
    attendance_id = Column(BigInteger, ForeignKey("attendance.id"))
    action = Column(Enum('CHECK_IN','CHECK_OUT'))
    action_time = Column(DateTime)