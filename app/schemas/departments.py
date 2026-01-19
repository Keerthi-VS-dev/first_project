from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class DepartmentCreate(BaseModel):
    department_name: str

class DepartmentUpdate(BaseModel):
    department_name: Optional[str] = None

class DepartmentResponse(BaseModel):
    id: int
    department_name: str
    created_at: datetime

    class Config:
        orm_mode = True
