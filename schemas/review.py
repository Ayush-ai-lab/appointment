from typing import Optional

from pydantic import BaseModel

class ReviewSchema(BaseModel):
    rating : int
    message : str
    created_by : Optional[str] = None
    updated_by : Optional[str] = None
    status: Optional[str] = None
