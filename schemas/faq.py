from pydantic import BaseModel

class faq(BaseModel):
    question : str
    answer : str