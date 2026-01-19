from datetime import date, datetime
from pydantic import BaseModel
from typing import Optional, Any

class EmployeeCreate(BaseModel):
    user_id: Optional[int] = None
    emp_code: str
    full_name: str
    department_id: Optional[int] = None
    designation: Optional[str] = None
    date_of_joining: Optional[date] = None
    skill_set: Optional[Any] = None
    certifications: Optional[Any] = None
    is_active: Optional[bool] = True

class EmployeeUpdate(BaseModel):
    emp_code: Optional[str] = None
    full_name: Optional[str] = None
    department_id: Optional[int] = None
    designation: Optional[str] = None
    date_of_joining: Optional[date] = None
    skill_set: Optional[Any] = None
    certifications: Optional[Any] = None
    is_active: Optional[bool] = None

class EmployeeResponse(BaseModel):
    id: int
    user_id: Optional[int]
    emp_code: str
    full_name: str
    department_id: Optional[int]
    designation: Optional[str]
    date_of_joining: Optional[date]
    skill_set: Optional[Any]
    certifications: Optional[Any]
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

