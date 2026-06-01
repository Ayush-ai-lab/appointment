from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.leave import LeaveSchema
from services.leave_service import create_leave, get_all_leave, get_single_leave, update_leave, delete_leave

router = APIRouter(prefix="/leave", tags=["leave"])


@router.post("/create-leave")
def CreateLeave(data: LeaveSchema, db: Session = Depends(get_db)):
    return create_leave(data, db)


@router.get("/")
def GetAllLeave(page: int = 1, limit: int = 12, search: str = None, status: str = None, doctor_id: int = None, specific_date: str = None, sort_by: str = "id", sort_order: str = "asc", db: Session = Depends(get_db)):
    return get_all_leave(db, page, limit, search, status, doctor_id, specific_date, sort_by, sort_order)


@router.get("/{id}")
def GetSingleLeave(id: int, db: Session = Depends(get_db)):
    return get_single_leave(id, db)


@router.put("/update-leave/{id}")
def UpdateLeave(id: int, data: LeaveSchema, db: Session = Depends(get_db)):
    return update_leave(id, data, db)


@router.delete("/delete-leave/{id}")
def DeleteLeave(id: int, db: Session = Depends(get_db)):
    return delete_leave(id, db)
