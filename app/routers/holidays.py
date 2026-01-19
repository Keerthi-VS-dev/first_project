from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
# from app.models.holiday import Holiday
from app.schemas.holidays import HolidayCreate, HolidayUpdate, HolidayResponse

router = APIRouter(prefix="/holidays", tags=["Holidays"])


@router.post("/", response_model=HolidayResponse)
def create_holiday(data: HolidayCreate, db: Session = Depends(get_db)):
    holiday = Holiday(**data.dict())
    db.add(holiday)
    db.commit()
    db.refresh(holiday)
    return holiday


@router.get("/", response_model=list[HolidayResponse])
def get_holidays(db: Session = Depends(get_db)):
    return db.query(Holiday).all()
