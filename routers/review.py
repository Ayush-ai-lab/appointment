from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.review import ReviewSchema
from services.review_service import create_review, get_all_review, get_single_review, update_review, delete_review

router = APIRouter(prefix="/review", tags=["review"])


@router.post("/create-review")
def CreateReview(data: ReviewSchema, db: Session = Depends(get_db)):
    return create_review(data, db)


@router.get("/")
def GetAllReview(page: int = 1, limit: int = 12, search: str = None, status: str = None, rating: int = None, sort_by: str = "id", sort_order: str = "asc", db: Session = Depends(get_db)):
    return get_all_review(db, page, limit, search, status, rating, sort_by, sort_order)


@router.get("/{id}")
def GetSingleReview(id: int, db: Session = Depends(get_db)):
    return get_single_review(id, db)


@router.put("/update-review/{id}")
def UpdateReview(id: int, data: ReviewSchema, db: Session = Depends(get_db)):
    return update_review(id, data, db)


@router.delete("/delete-review/{id}")
def DeleteReview(id: int, db: Session = Depends(get_db)):
    return delete_review(id, db)
