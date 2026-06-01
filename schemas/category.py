from typing import Optional

from pydantic import BaseModel

class CategorySchema(BaseModel):
    name : str
    department_id: int
    slug: str
    short_description : str
    description : str 
    status : str 
    created_by: Optional[str] = None
    updated_by: Optional[str] = None

