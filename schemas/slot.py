from datetime import time
from typing import Optional

from pydantic import BaseModel


class SlotSchema(BaseModel):
    status: str
    doctor_id: int
    slot_start: time
    slot_end: time
    slot_date: str
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
