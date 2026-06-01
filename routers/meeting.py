from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.meeting import MeetingSchema
from services.meeting_service import create_meeting, get_all_meeting, get_single_meeting, update_meeting, delete_meeting

router = APIRouter(prefix="/meeting", tags=["meeting"])


@router.post("/create-meeting")
def CreateMeeting(data: MeetingSchema, db: Session = Depends(get_db)):
    return create_meeting(data, db)


@router.get("/")
def GetAllMeeting(page: int = 1, limit: int = 12, search: str = None, status: str = None, sort_by: str = "id", sort_order: str = "asc", db: Session = Depends(get_db)):
    return get_all_meeting(db, page, limit, search, status, sort_by, sort_order)


@router.get("/{id}")
def GetSingleMeeting(id: int, db: Session = Depends(get_db)):
    return get_single_meeting(id, db)


@router.put("/update-meeting/{id}")
def UpdateMeeting(id: int, data: MeetingSchema, db: Session = Depends(get_db)):
    return update_meeting(id, data, db)


@router.delete("/delete-meeting/{id}")
def DeleteMeeting(id: int, db: Session = Depends(get_db)):
    return delete_meeting(id, db)
