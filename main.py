from fastapi import FastAPI

from app.database import engine
from app.models import employee, attendance   # ✅ MODELS ONLY
from app.routers import employees, attendance as attendance_router

app = FastAPI(title="FastAPI Attendance CRUD")

# ✅ CREATE TABLES (ONLY FROM MODELS)
employee.Base.metadata.create_all(bind=engine)
attendance.Base.metadata.create_all(bind=engine)

# ✅ REGISTER ROUTERS
app.include_router(employees.router)
app.include_router(attendance_router.router)

