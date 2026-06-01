from typing import Optional

from pydantic import BaseModel

class DoctorSchema(BaseModel):
    name : str
    email : str
    number : int 
    experience : int 
    qualification : str 
    bio : str 
    category_id: Optional[int] = None
    status: Optional[str] = None
    created_by : Optional[str] = None
    updated_by : Optional[str] = None


