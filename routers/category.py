from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.category import CategorySchema
from services.category_service import create_category, get_all_category, get_single_category, update_category, delete_category

router = APIRouter(prefix="/category", tags=["category"])


@router.post("/create-category")
def CreateCategory(data: CategorySchema, db: Session = Depends(get_db)):
    return create_category(data, db)


@router.get("/")
def GetAllCategory(page: int = 1, limit: int = 12, search: str = None, status: str = None, department_id: int = None, sort_by: str = "id", sort_order: str = "asc", db: Session = Depends(get_db)):
    return get_all_category(db, page, limit, search, status, department_id, sort_by, sort_order)


@router.get("/{id}")
def GetSingleCategory(id: int, db: Session = Depends(get_db)):
    return get_single_category(id, db)


@router.put("/update-category/{id}")
def UpdateCategory(id: int, data: CategorySchema, db: Session = Depends(get_db)):
    return update_category(id, data, db)


@router.delete("/delete-category/{id}")
def DeleteCategory(id: int, db: Session = Depends(get_db)):
    return delete_category(id, db)
