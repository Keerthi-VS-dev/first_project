from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class EmployeeCreate(BaseModel):
    employee_id: str
    name: str
    email: EmailStr
    password: str
    designation: Optional[str] = None
    role: Optional[str] = "employee"
    is_active: Optional[bool] = True

class EmployeeResponse(BaseModel):
    id: int
    employee_id: str
    name: str
    email: EmailStr
    role: str
    designation: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
