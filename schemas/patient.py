from typing import Optional

from pydantic import BaseModel


class PatientHistorySchema(BaseModel):
    user_id: int
    email: Optional[str] = None
    mobile_number: Optional[str] = None
    registration_number: Optional[str] = None
    doctor_id: int
    appointment_id: int
    symptoms: Optional[str] = None
    diagnosis: Optional[str] = None
    prescription: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
    status: Optional[str] = None
