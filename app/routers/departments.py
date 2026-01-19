from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
# from app.models.department import Department
from app.schemas.departments import DepartmentCreate, DepartmentUpdate, DepartmentResponse

router = APIRouter(prefix="/departments", tags=["Departments"])


@router.post("/", response_model=DepartmentResponse)
def create_department(data: DepartmentCreate, db: Session = Depends(get_db)):
    department = Department(**data.dict())
    db.add(department)
    db.commit()
    db.refresh(department)
    return department


@router.get("/", response_model=list[DepartmentResponse])
def get_departments(db: Session = Depends(get_db)):
    return db.query(Department).all()


@router.get("/{department_id}", response_model=DepartmentResponse)
def get_department(department_id: int, db: Session = Depends(get_db)):
    department = db.query(Department).get(department_id)
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")
    return department


@router.put("/{department_id}", response_model=DepartmentResponse)
def update_department(department_id: int, data: DepartmentUpdate, db: Session = Depends(get_db)):
    department = db.query(Department).get(department_id)
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(department, key, value)

    db.commit()
    db.refresh(department)
    return department


@router.delete("/{department_id}")
def delete_department(department_id: int, db: Session = Depends(get_db)):
    department = db.query(Department).get(department_id)
    if not department:
        raise HTTPException(status_code=404, detail="Department not found")

    db.delete(department)
    db.commit()
    return {"message": "Department deleted"}
