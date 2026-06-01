from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.leave import LeaveSchema
from services.leave_service import (
    create_leave,
    delete_leave,
    get_all_leave,
    get_single_leave,
    update_leave,
)


router = APIRouter(prefix="/leave", tags=["leave"])


@router.post("/create-leave")
def CreateLeave(data: LeaveSchema, db: Session = Depends(get_db)):
    return create_leave(data, db)


@router.get("/")
def GetAllLeave(db: Session = Depends(get_db)):
    return get_all_leave(db)


@router.get("/{id}")
def GetSingleLeave(id: int, db: Session = Depends(get_db)):
    return get_single_leave(id, db)


@router.put("/update-leave/{id}")
def UpdateLeave(id: int, data: LeaveSchema, db: Session = Depends(get_db)):
    return update_leave(id, data, db)


@router.delete("/delete-leave/{id}")
def DeleteLeave(id: int, db: Session = Depends(get_db)):
    return delete_leave(id, db)
