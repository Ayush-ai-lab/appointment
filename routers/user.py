from fastapi import APIRouter, Depends, UploadFile, File, Form 
from sqlalchemy.orm import Session
import os
import shutil
import uuid
from core.database import get_db
from schemas.user import UserSchemas
from services.user_service import create_user, update_user, get_all_user, get_single_user, delete_user

router = APIRouter(prefix="/user", tags=["user"])


# @router.post("/create-user")
# def CreateUser(data: UserSchemas, db: Session = Depends(get_db)):
#     return create_user(data, db)
@router.post("/create-user")
async def CreateUser(
    name: str = Form(...),
    email: str = Form(...),
    number: int = Form(...),
    password: str = Form(...),
    age: int = Form(...),
    profile_image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    return await create_user(
        name,
        email,
        number,
        password,
        age,
        profile_image,
        db
    )

def UpdateUser(
    id: int,
    name: str = Form(...),
    email: str = Form(...),
    number: int = Form(...),
    password: str = Form(...),
    age: int = Form(...),
    updated_by: str = Form(...),
    status: str = Form(...),
    profile_image: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    return update_user(
        id=id,
        name=name,
        email=email,
        number=number,
        password=password,
        age=age,
        updated_by=updated_by,
        status=status,
        profile_image=profile_image,
        db=db
    )

@router.get("/")
def GetAllUser(page: int = 1, limit: int = 12, search: str = None, status: str = None, sort_by: str = "id", sort_order: str = "asc", db: Session = Depends(get_db)):
    return get_all_user(db, page, limit, search, status, sort_by, sort_order)


@router.get("/{id}")
def GetSingleUser(id: int, db: Session = Depends(get_db)):
    return get_single_user(id, db)


@router.delete("/delete-user/{id}")
def DeleteUser(id: int, db: Session = Depends(get_db)):
    return delete_user(id, db)
