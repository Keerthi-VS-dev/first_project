
from datetime import date, datetime
from decimal import Decimal
from enum import Enum as PyEnum
from pydantic import BaseModel
from typing import Optional


# Optional: Define the status as a Python Enum for Pydantic
class AttendanceStatus(str, PyEnum):
    PRESENT = "PRESENT"
    ABSENT = "ABSENT"
    HALF_DAY = "HALF_DAY"


# Schema for creating a new attendance record
class AttendanceCreate(BaseModel):
    employee_id: int
    date: date
    check_in_time: Optional[datetime] = None
    check_out_time: Optional[datetime] = None
    worked_hours: Optional[Decimal] = None
    status: AttendanceStatus

# Schema for updating an attendance record
class AttendanceUpdate(BaseModel):
    check_in_time: Optional[datetime] = None
    check_out_time: Optional[datetime] = None
    worked_hours: Optional[Decimal] = None
    status: Optional[AttendanceStatus] = None

# Schema for reading attendance (response)
class AttendanceResponse(BaseModel):
    id: int
    employee_id: int
    date: date
    check_in_time: Optional[datetime] = None
    check_out_time: Optional[datetime] = None
    worked_hours: Optional[Decimal] = None
    status: AttendanceStatus
    created_at: datetime

    class Config:
        orm_mode = True
