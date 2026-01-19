from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date

# ---------- Base Schemas ----------
class AttendanceBase(BaseModel):
    date: date
    status: Optional[str] = "absent"

class AttendanceCreate(AttendanceBase):
    employee_id: str

class AttendanceUpdate(BaseModel):
    check_in: Optional[datetime] = None
    check_out: Optional[datetime] = None
    status: Optional[str] = None

# ---------- Response Schemas ----------
class AttendanceResponse(BaseModel):
    id: int
    employee_id: int
    employee_name: str
    date: date
    status: Optional[str] = None
    check_in: Optional[datetime] = None
    check_out: Optional[datetime] = None
    total_hours: float
    created_at: datetime                 # required
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class AttendanceList(BaseModel):
    attendance: List[AttendanceResponse]
    total: int

# ---------- Check-in / Check-out ----------
class CheckInOut(BaseModel):
    employee_id : str

class CheckInOutResponse(BaseModel):
    message: str
    attendance_id: int
    check_in: Optional[datetime] = None
    check_out: Optional[datetime] = None

# ---------- Today Attendance ----------
class TodayAttendanceResponse(BaseModel):
    date: date
    status: str
    check_in: Optional[datetime] = None
    check_out: Optional[datetime] = None
