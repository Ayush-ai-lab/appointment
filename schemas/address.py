from typing import Optional

from pydantic import BaseModel

class AddressSchema(BaseModel):
    country : str
    state : str 
    city : str 
    street_address : str
    address : str
    pin_code: int
    user_id: Optional[int] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
    status: Optional[str] = None
