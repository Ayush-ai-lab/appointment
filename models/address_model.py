from core.database import Base 
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from datetime import datetime

class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    country = Column(String)
    state = Column(String)
    city = Column(String)
    Street_Address = Column(String)
    Address = Column(String)

    