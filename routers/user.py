from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.user import UserSchemas
from services.user_service import create_user, update_user, get_all_user, get_single_user, delete_user

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/create-user")
def CreateUser(data: UserSchemas, db: Session = Depends(get_db)):
    return create_user(data, db)


@router.put("/update-user/{id}")
def UpdateUser(id: int, data: UserSchemas, db: Session = Depends(get_db)):
    return update_user(id, data, db)


@router.get("/")
def GetAllUser(page: int = 1, limit: int = 12, search: str = None, status: str = None, sort_by: str = "id", sort_order: str = "asc", db: Session = Depends(get_db)):
    return get_all_user(db, page, limit, search, status, sort_by, sort_order)


@router.get("/{id}")
def GetSingleUser(id: int, db: Session = Depends(get_db)):
    return get_single_user(id, db)


@router.delete("/delete-user/{id}")
def DeleteUser(id: int, db: Session = Depends(get_db)):
    return delete_user(id, db)
