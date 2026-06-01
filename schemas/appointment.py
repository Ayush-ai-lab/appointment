from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AppointmentSchema(BaseModel):
    status: str
    department_id: int
    user_id: int
    category_id: int
    short_description: str
    appointment_date: datetime
    appointment_status: int
    payment_status: int
    notes: Optional[str] = None
    symptoms: Optional[str] = None
    doctor_id: Optional[int] = None
    slot_id: Optional[int] = None
    appointment_valid_date: Optional[datetime] = None
    prescription: Optional[str] = None
    meeting_id: Optional[int] = None
    weight: Optional[int] = None
    bp: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
