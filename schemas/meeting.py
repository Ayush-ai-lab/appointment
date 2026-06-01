from typing import Optional

from pydantic import BaseModel


class MeetingSchema(BaseModel):
    name: str
    url: str
    status: str
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
