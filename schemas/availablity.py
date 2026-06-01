from datetime import time
from typing import Optional

from pydantic import BaseModel


class AvailabilitySchema(BaseModel):
    status: str
    doctor_id: int
    day_of_week: str
    start_time: time
    end_time: time
    slot_interval: int
    break_start: Optional[time] = None
    break_end: Optional[time] = None
    leave_id: Optional[int] = None
    specific_date: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
