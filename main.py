

from fastapi import FastAPI
from app.routers import (
    users, employees, departments,
    attendance, education, experience, holidays
)

app = FastAPI(title="Attendance Management System")

app.include_router(users.router)
app.include_router(departments.router)
app.include_router(employees.router)
app.include_router(attendance.router)
app.include_router(education.router)
app.include_router(experience.router)
app.include_router(holidays.router)
