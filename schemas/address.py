from pydantic import BaseModel 

class AddressSchema(BaseModel):
    Country : str
    State : str 
    City : str 
    street_address : str
    address : str