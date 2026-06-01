from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.slot import SlotSchema
from services.slot_service import create_slot, get_all_slot, get_single_slot, update_slot, delete_slot

router = APIRouter(prefix="/slot", tags=["slot"])


@router.post("/create-slot")
def CreateSlot(data: SlotSchema, db: Session = Depends(get_db)):
    return create_slot(data, db)


@router.get("/")
def GetAllSlot(page: int = 1, limit: int = 12, search: str = None, status: str = None, doctor_id: int = None, slot_date: str = None, sort_by: str = "id", sort_order: str = "asc", db: Session = Depends(get_db)):
    return get_all_slot(db, page, limit, search, status, doctor_id, slot_date, sort_by, sort_order)


@router.get("/{id}")
def GetSingleSlot(id: int, db: Session = Depends(get_db)):
    return get_single_slot(id, db)


@router.put("/update-slot/{id}")
def UpdateSlot(id: int, data: SlotSchema, db: Session = Depends(get_db)):
    return update_slot(id, data, db)


@router.delete("/delete-slot/{id}")
def DeleteSlot(id: int, db: Session = Depends(get_db)):
    return delete_slot(id, db)
