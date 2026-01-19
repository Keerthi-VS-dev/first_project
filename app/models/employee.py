
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String(50), unique=True, index=True, nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    designation = Column(String(100), nullable=True)
    role = Column(String(50), nullable=False, default="employee")
    skillset = Column(JSON, nullable=True)
    certification = Column(JSON, nullable=True)
    holiday_plan = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    force_password_change = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Relationship
    attendance_records = relationship("Attendance", back_populates="employee")

