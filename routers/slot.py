from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.slot import SlotSchema
from services.slot_service import (
    create_slot,
    delete_slot,
    get_all_slot,
    get_single_slot,
    update_slot,
)


router = APIRouter(prefix="/slot", tags=["slot"])


@router.post("/create-slot")
def CreateSlot(data: SlotSchema, db: Session = Depends(get_db)):
    return create_slot(data, db)


@router.get("/")
def GetAllSlot(db: Session = Depends(get_db)):
    return get_all_slot(db)


@router.get("/{id}")
def GetSingleSlot(id: int, db: Session = Depends(get_db)):
    return get_single_slot(id, db)


@router.put("/update-slot/{id}")
def UpdateSlot(id: int, data: SlotSchema, db: Session = Depends(get_db)):
    return update_slot(id, data, db)


@router.delete("/delete-slot/{id}")
def DeleteSlot(id: int, db: Session = Depends(get_db)):
    return delete_slot(id, db)
