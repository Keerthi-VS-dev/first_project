from sqlalchemy import Column, BigInteger, String, Date, Boolean, JSON, ForeignKey, DateTime
from app.database import Base


class Employee(Base):
    __tablename__ = "employees"


    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, ForeignKey("users.id"))
    emp_code = Column(String(50))
    full_name = Column(String(100))
    department_id = Column(BigInteger, ForeignKey("departments.id"))
    designation = Column(String(100))
    date_of_joining = Column(Date)
    skill_set = Column(JSON)
    certifications = Column(JSON)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())