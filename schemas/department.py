from pydantic import BaseModel

class DepartmentSchemas(BaseModel):
    name : str 
    slug : str
    icon : str
    image : str
    status : str 
    created_by : str
    
