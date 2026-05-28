from fastapi import Depends, APIRouter 
from schemas.doctor import DoctorSchema 
from core.database import get_db 
from sqlalchemy.orm import Session 
from services.doctor_service import create_doctor, get_all_doctor, get_single_doctor, update_doctor, delete_doctor

router = APIRouter(prefix="/doctor", tags=["doctor"])

@router.post("/create-doctor")
def CreateRoute(data : DoctorSchema, db: Session  = Depends(get_db)):
    return create_doctor(data, db)

@router.get("/")
def GetAll(db: Session = Depends(get_db)):
    return get_all_doctor(db)

@router.get("/{id}")
def GetSingleDoctor(id : int, db:Session = Depends(get_db)):
    return get_single_doctor(id, db)

@router.put("/update-route/{id}")
def UpdateDoctor(id: int,data :DoctorSchema, db:Session = Depends(get_db)):
    return update_doctor(id,data, db)

@router.delete("/delete-route/{id}")
def DeleteDoctor(id: int, db: Session = Depends(get_db)):
    return delete_doctor(id, db)