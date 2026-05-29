from core.database import get_db
from  services.user_service import create_user, update_user, get_all_user, get_single_user, delete_user
from sqlalchemy.orm import Session 
from fastapi import APIRouter, Depends
from schemas.user import UserSchemas

router = APIRouter(prefix="/user", tags=["user"])

@router.post("/create-user")
def CreateUser(data: UserSchemas, db:Session= Depends(get_db)):
    return create_user(data, db)

@router.post("/update-user")
def UpdateUser(id : int, data:UserSchemas, db:Session= Depends(get_db)):
    return update_user(id, data, db)

@router.get("/")
def GetAllUser( db:Session = Depends(get_db)):
    return get_all_user(db)

@router.get("/{id}")
def GetSingleUser(id : int, db:Session = Depends(get_db)):
    return get_single_user(id, db)

@router.delete("delete-user/{id}")
def DeleteUser(id :int, db:Session = Depends(get_db)):
    return delete_user(id,db)