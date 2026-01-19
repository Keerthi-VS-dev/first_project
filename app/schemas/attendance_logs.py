from datetime import datetime
from enum import Enum as PyEnum
from pydantic import BaseModel
from typing import Optional

class AttendanceAction(str, PyEnum):
    CHECK_IN = "CHECK_IN"
    CHECK_OUT = "CHECK_OUT"

class AttendanceLogCreate(BaseModel):
    attendance_id: int
    action: AttendanceAction
    action_time: datetime

class AttendanceLogUpdate(BaseModel):
    action: Optional[AttendanceAction] = None
    action_time: Optional[datetime] = None

class AttendanceLogResponse(BaseModel):
    id: int
    attendance_id: int
    action: AttendanceAction
    action_time: datetime

    class Config:
        orm_mode = True
