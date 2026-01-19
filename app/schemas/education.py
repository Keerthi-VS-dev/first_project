from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class EducationCreate(BaseModel):
    employee_id: int
    degree: str
    specialization: Optional[str] = None
    institution: str
    years_of_passing: int
    grade_or_cgpa: Optional[str] = None

class EducationUpdate(BaseModel):
    degree: Optional[str] = None
    specialization: Optional[str] = None
    institution: Optional[str] = None
    years_of_passing: Optional[int] = None
    grade_or_cgpa: Optional[str] = None

class EducationResponse(BaseModel):
    id: int
    employee_id: int
    degree: str
    specialization: Optional[str]
    institution: str
    years_of_passing: int
    grade_or_cgpa: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
