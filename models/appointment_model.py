from core.database import Base 
from sqlalchemy import Column, String, Integer, ForeignKey 

class Appointment(Base):
    __tablename__ = "appointment"

    id = Column(Integer, primary_key=True)
    