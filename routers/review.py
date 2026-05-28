from schemas.review import ReviewSchema
from core.database import get_db
from services.review_service import create_review, get_all_review, get_single_reviw, update_review,delete_review
from fastapi import APIRouter, Depends 
from sqlalchemy.orm import Session

router = APIRouter(prefix="/review", tags="review")

@router.post("/create-review")
def CreateReview(data: ReviewSchema, db: Session = Depends(get_db)):
    return create_review(data, db)



def GetAllReview(db: Session = Depends(get_db)):
    return get_all_review(db)

def GetSingleReview(id: int, db: Session = Depends(get_db)):
    return get_single_review(id,db)

def UpdateReview(id : int, data: ReviewSchema, db: Session = Depends(get_db)):
    return update_review(id, data, db)

def DeleteReview(id: int, db : Session = Depends(get_db)):
    return delete_review(id, db)