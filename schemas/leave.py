from datetime import date
from typing import Optional

from pydantic import BaseModel


class LeaveSchema(BaseModel):
    doctor_id: int
    specific_date: date
    status: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
