from pydantic import BaseModel 

class AddressSchema(BaseModel):
    country : str
    state : str 
    city : str 
    street_address : str
    address : str
    pin_code: int