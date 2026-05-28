from pydantic import BaseModel

class DoctorSchema(BaseModel):
    name : str
    email : str
    number : int 
    experience : int 
    qualification : str 
    bio : str 
    created_by : str
    updated_by : str 


