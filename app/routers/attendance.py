# app/routers/attendance.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import and_
from datetime import datetime, date, timezone, timedelta
from app.database import get_db
from app.models.attendance import Attendance
from app.models.employee import Employee
from app.schemas.attendance import (
    CheckInOut,
    CheckInOutResponse,
    TodayAttendanceResponse,
    AttendanceResponse,
)

router = APIRouter(prefix="/attendance", tags=["Attendance"])

# IST timezone
IST = timezone(timedelta(hours=5, minutes=30))

# -------------------- Helpers --------------------

def make_aware(dt: datetime) -> datetime:
    """Convert naive datetime to IST-aware"""
    if dt is None:
        return None
    if dt.tzinfo is None:
        return dt.replace(tzinfo=IST)
    return dt

def calculate_total_hours(check_in: datetime, check_out: datetime) -> float:
    """Calculate hours between two datetimes safely"""
    check_in = make_aware(check_in)
    check_out = make_aware(check_out)
    if not check_in or not check_out:
        return 0.0
    return round((check_out - check_in).total_seconds() / 3600, 2)

# -------------------- Check-in --------------------

@router.post("/check-in", response_model=CheckInOutResponse)
def check_in(request: CheckInOut, db: Session = Depends(get_db)):
    # get employee by string employee_id
    employee = db.query(Employee).filter(Employee.employee_id == request.employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    today = datetime.now(IST).date()
    now = datetime.now(IST)

    attendance = db.query(Attendance).filter(
        and_(Attendance.employee_id == employee.id, Attendance.date == today)
    ).first()

    if attendance and attendance.check_in:
        raise HTTPException(status_code=400, detail="Already checked in today")

    if attendance:
        attendance.check_in = now
        attendance.status = "present"
    else:
        attendance = Attendance(employee_id=employee.id, date=today, check_in=now, status="present")
        db.add(attendance)

    db.commit()
    db.refresh(attendance)

    return CheckInOutResponse(
        message="Checked in successfully",
        attendance_id=attendance.id,
        check_in=attendance.check_in
    )

# -------------------- Check-out --------------------

@router.post("/check-out", response_model=CheckInOutResponse)
def check_out(request: CheckInOut, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.employee_id == request.employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    today = datetime.now(IST).date()
    now = datetime.now(IST)

    attendance = db.query(Attendance).filter(
        and_(Attendance.employee_id == employee.id, Attendance.date == today)
    ).first()

    if not attendance or not attendance.check_in:
        raise HTTPException(status_code=400, detail="No check-in record found for today")
    if attendance.check_out:
        raise HTTPException(status_code=400, detail="Already checked out today")

    attendance.check_out = now
    attendance.total_hours = calculate_total_hours(attendance.check_in, now)

    db.commit()
    db.refresh(attendance)

    return CheckInOutResponse(
        message="Checked out successfully",
        attendance_id=attendance.id,
        check_out=attendance.check_out
    )

# -------------------- Today's attendance --------------------

@router.get("/today/{employee_id}", response_model=TodayAttendanceResponse)
def get_today_attendance(employee_id: str, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.employee_id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    today = datetime.now(IST).date()
    attendance = db.query(Attendance).filter(
        and_(Attendance.employee_id == employee.id, Attendance.date == today)
    ).first()

    if not attendance:
        return TodayAttendanceResponse(date=today, status="not_checked_in")

    return TodayAttendanceResponse(
        date=attendance.date,
        status=attendance.status,
        check_in=attendance.check_in,
        check_out=attendance.check_out
    )

# -------------------- All attendance --------------------

@router.get("/all", response_model=list[AttendanceResponse])
def get_all_attendance(db: Session = Depends(get_db)):
    # join attendance with employee to get name and employee_id string
    results = db.query(Attendance, Employee).join(Employee, Attendance.employee_id == Employee.id).all()

    response = [
        AttendanceResponse(
            id=att.id,
            employee_id=emp.employee_id,  # string employee_id
            employee_name=emp.name,  # employee name
            date=att.date,
            status=att.status,
            check_in=att.check_in,
            check_out=att.check_out,
            total_hours=att.total_hours,
            created_at=att.created_at,  # <-- include this
            updated_at=att.updated_at  # <-- include optional updated_at
        )
        for att, emp in results
    ]

    return response
