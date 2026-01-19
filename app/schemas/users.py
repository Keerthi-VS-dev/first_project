from datetime import datetime
from enum import Enum as PyEnum
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserRole(str, PyEnum):
    ADMIN = "ADMIN"
    EMPLOYEE = "EMPLOYEE"
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: UserRole
    is_active: Optional[bool] = True
class UserUpdate(BaseModel):
    role: Optional[UserRole] = None
    is_active: Optional[bool] = None
    last_login: Optional[datetime] = None
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: UserRole
    is_active: bool
    last_login: Optional[datetime]
    created_at: datetime

    class Config:
        orm_mode = True
class UserInDB(UserResponse):
    password_hashed: str

