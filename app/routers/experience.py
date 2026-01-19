from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
# from app.models.experience import Experience
from app.schemas.experience import ExperienceCreate, ExperienceUpdate, ExperienceResponse

router = APIRouter(prefix="/experience", tags=["Experience"])


@router.post("/", response_model=ExperienceResponse)
def create_experience(data: ExperienceCreate, db: Session = Depends(get_db)):
    exp = Experience(**data.dict())
    db.add(exp)
    db.commit()
    db.refresh(exp)
    return exp


@router.get("/", response_model=list[ExperienceResponse])
def get_experience(db: Session = Depends(get_db)):
    return db.query(Experience).all()
