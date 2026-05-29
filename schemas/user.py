from pydantic import BaseModel 

class UserSchemas(BaseModel):
    name: str
    email : str
    number : str
    password: str
    age : int    