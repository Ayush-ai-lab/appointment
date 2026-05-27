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
    street_Address = Column(String)
    address = Column(String)
    pin_code = Column(Integer)

    