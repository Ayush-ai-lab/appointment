from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.availablity import AvailabilitySchema
from services.availablity_service import create_availability, get_all_availability, get_single_availability, update_availability, delete_availability

router = APIRouter(prefix="/availability", tags=["availability"])


@router.post("/create-availability")
def CreateAvailability(data: AvailabilitySchema, db: Session = Depends(get_db)):
    return create_availability(data, db)


@router.get("/")
def GetAllAvailability(page: int = 1, limit: int = 12, search: str = None, status: str = None, doctor_id: int = None, day_of_week: str = None, specific_date: str = None, sort_by: str = "id", sort_order: str = "asc", db: Session = Depends(get_db)):
    return get_all_availability(db, page, limit, search, status, doctor_id, day_of_week, specific_date, sort_by, sort_order)


@router.get("/{id}")
def GetSingleAvailability(id: int, db: Session = Depends(get_db)):
    return get_single_availability(id, db)


@router.put("/update-availability/{id}")
def UpdateAvailability(id: int, data: AvailabilitySchema, db: Session = Depends(get_db)):
    return update_availability(id, data, db)


@router.delete("/delete-availability/{id}")
def DeleteAvailability(id: int, db: Session = Depends(get_db)):
    return delete_availability(id, db)
