from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.database import get_db
from schemas.patient import PatientHistorySchema
from services.patient_service import create_patient_history, delete_patient_history, get_all_patient_history, get_single_patient_history, update_patient_history

router = APIRouter(prefix="/patient-history", tags=["patient-history"])


@router.post("/create-patient-history")
def CreatePatientHistory(data: PatientHistorySchema, db: Session = Depends(get_db)):
    return create_patient_history(data, db)


@router.get("/")
def GetAllPatientHistory(page: int = 1, limit: int = 12, search: str = None, doctor_id: int = None, user_id: int = None, status: str = None, sort_by: str = "id", sort_order: str = "asc", db: Session = Depends(get_db)):
    return get_all_patient_history(db, page, limit, search, doctor_id, user_id, status, sort_by, sort_order)


@router.get("/{id}")
def GetSinglePatientHistory(id: int, db: Session = Depends(get_db)):
    return get_single_patient_history(id, db)


@router.put("/update-patient-history/{id}")
def UpdatePatientHistory(id: int, data: PatientHistorySchema, db: Session = Depends(get_db)):
    return update_patient_history(id, data, db)


@router.delete("/delete-patient-history/{id}")
def DeletePatientHistory(id: int, db: Session = Depends(get_db)):
    return delete_patient_history(id, db)
