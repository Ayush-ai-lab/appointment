from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.appointment import AppointmentSchema
from services.appointment_service import (
    create_appointment,
    delete_appointment,
    get_all_appointment,
    get_single_appointment,
    update_appointment,
)


router = APIRouter(prefix="/appointment", tags=["appointment"])


@router.post("/create-appointment")
def CreateAppointment(data: AppointmentSchema, db: Session = Depends(get_db)):
    return create_appointment(data, db)


@router.get("/")
def GetAllAppointment(db: Session = Depends(get_db)):
    return get_all_appointment(db)


@router.get("/{id}")
def GetSingleAppointment(id: int, db: Session = Depends(get_db)):
    return get_single_appointment(id, db)


@router.put("/update-appointment/{id}")
def UpdateAppointment(id: int, data: AppointmentSchema, db: Session = Depends(get_db)):
    return update_appointment(id, data, db)


@router.delete("/delete-appointment/{id}")
def DeleteAppointment(id: int, db: Session = Depends(get_db)):
    return delete_appointment(id, db)
