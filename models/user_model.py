from sqlalchemy import Column, Integer, String, ForeignKey 
from core.database import Base 

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    number = Column(Integer)
    password = Column(String)