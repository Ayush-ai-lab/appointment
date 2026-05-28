from pydantic import BaseModel 

class ReviewSchema(BaseModel):
    rating : int
    message : str
    created_by : str 