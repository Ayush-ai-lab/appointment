from fastapi import APIRouter,Depends
from schemas.address import AddressSchema
from services.address_service import Add_address, update_address, get_all_address, get_single_address, delete_address
from core.database import get_db

from sqlalchemy.orm import Session


routes = APIRouter(prefix="/address", tags=["address"])

@routes.post("/create-address")
def CreateAddress(address : AddressSchema, db: Session = Depends(get_db)):
    return Add_address(address, db)

@routes.post("/update-address/{id}")
def UpdateAddress(id : int, address: AddressSchema, db: Session = Depends(get_db) ):
    return update_address(id, address,db)

@routes.get("/")
def GetAll(db: Session = Depends(get_db)):
    return get_all_address(db)

@routes.get("/{id}")        
def Get_Single_Address(id : int,  db: Session = Depends(get_db)):
    return get_single_address(id, db)

@routes.delete("/delete-address/{id}")
def DeleteUser(id : int, db: Session = Depends(get_db)):
    return delete_address(id, db)
