from pydantic import BaseModel 

class CategorySchema(BaseModel):
    name : str
    short_description : str
    description : str 
    status : str 

