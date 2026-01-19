

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.sql import func
from app.database import Base  # Make sure Base is imported from your database.py

class Education(Base):
    __tablename__ = "educations"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"), nullable=False)
    degree = Column(String(255), nullable=False)
    specialization = Column(String(255), nullable=True)
    institution = Column(String(255), nullable=False)
    years_of_passing = Column(Integer, nullable=False)
    grade_or_cgpa = Column(String(50), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
