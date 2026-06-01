from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.address import AddressSchema
from services.address_service import Add_address, update_address, get_all_address, get_single_address, delete_address

routes = APIRouter(prefix="/address", tags=["address"])


@routes.post("/create-address")
def CreateAddress(address: AddressSchema, db: Session = Depends(get_db)):
    return Add_address(address, db)


@routes.post("/update-address/{id}")
def UpdateAddress(id: int, address: AddressSchema, db: Session = Depends(get_db)):
    return update_address(id, address, db)


@routes.get("/")
def GetAll(page: int = 1, limit: int = 12, search: str = None, status: str = None, user_id: int = None, sort_by: str = "id", sort_order: str = "asc", db: Session = Depends(get_db)):
    return get_all_address(db, page, limit, search, status, user_id, sort_by, sort_order)


@routes.get("/{id}")
def Get_Single_Address(id: int, db: Session = Depends(get_db)):
    return get_single_address(id, db)


@routes.delete("/delete-address/{id}")
def DeleteUser(id: int, db: Session = Depends(get_db)):
    return delete_address(id, db)
