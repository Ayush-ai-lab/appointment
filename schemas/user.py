from typing import Optional

from pydantic import BaseModel

class UserSchemas(BaseModel):
    name: str
    email : str
    number : int
    password: str
    age : int    
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
    status: Optional[str] = None
