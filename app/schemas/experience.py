from datetime import date, datetime
from pydantic import BaseModel
from typing import Optional

class ExperienceCreate(BaseModel):
    employee_id: int
    company_name: str
    job_title: str
    start_date: date
    end_date: Optional[date] = None
    years_of_experience: float

class ExperienceUpdate(BaseModel):
    company_name: Optional[str] = None
    job_title: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    years_of_experience: Optional[float] = None

class ExperienceResponse(BaseModel):
    id: int
    employee_id: int
    company_name: str
    job_title: str
    start_date: date
    end_date: Optional[date]
    years_of_experience: float
    created_at: datetime

    class Config:
        orm_mode = True
