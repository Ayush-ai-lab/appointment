from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.faq import FaqSchema
from services.faq_service import create_faq, get_all_faq, get_single_faq, update_faq, delete_faq

router = APIRouter(prefix="/faq", tags=["faq"])


@router.post("/create-faq")
def CreateFaq(data: FaqSchema, db: Session = Depends(get_db)):
    return create_faq(data, db)


@router.get("/")
def GetAllFaq(page: int = 1, limit: int = 12, search: str = None, status: str = None, sort_by: str = "id", sort_order: str = "asc", db: Session = Depends(get_db)):
    return get_all_faq(db, page, limit, search, status, sort_by, sort_order)


@router.get("/{id}")
def GetSingleFaq(id: int, db: Session = Depends(get_db)):
    return get_single_faq(id, db)


@router.put("/update-faq/{id}")
def UpdateFaq(id: int, data: FaqSchema, db: Session = Depends(get_db)):
    return update_faq(id, data, db)


@router.delete("/delete-faq/{id}")
def DeleteFaq(id: int, db: Session = Depends(get_db)):
    return delete_faq(id, db)
