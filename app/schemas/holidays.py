from datetime import date, datetime
from pydantic import BaseModel
from typing import Optional

class HolidayCreate(BaseModel):
    date: date
    day: str
    holiday_name: str
    is_optional: Optional[bool] = False

class HolidayUpdate(BaseModel):
    date: Optional[date] = None
    day: Optional[str] = None
    holiday_name: Optional[str] = None
    is_optional: Optional[bool] = None

class HolidayResponse(BaseModel):
    id: int
    date: date
    day: str
    holiday_name: str
    is_optional: bool
    created_at: datetime

    class Config:
        orm_mode = True

