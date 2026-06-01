from typing import Optional

from pydantic import BaseModel

class DepartmentSchemas(BaseModel):
    name : str 
    slug : str
    icon : str
    image : str
    status : str 
    created_by : Optional[str] = None
    updated_by : Optional[str] = None
    
