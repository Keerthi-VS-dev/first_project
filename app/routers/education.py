from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
# from app.models.education import Education
from app.schemas.education import EducationCreate, EducationUpdate, EducationResponse

router = APIRouter(prefix="/education", tags=["Education"])


@router.post("/", response_model=EducationResponse)
def create_education(data: EducationCreate, db: Session = Depends(get_db)):
    edu = Education(**data.dict())
    db.add(edu)
    db.commit()
    db.refresh(edu)
    return edu


@router.get("/", response_model=list[EducationResponse])
def get_education(db: Session = Depends(get_db)):
    return db.query(Education).all()
