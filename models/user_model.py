from sqlalchemy import Column, Integer, String, ForeignKey, DateTime 
from core.database import Base 
from datetime import datetime
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    number = Column(Integer)
    password = Column(String)
    age = Column(Integer)
    created_by = Column(String)
    updated_by = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    address = relationship("Address", back_populates="user")
    appointments = relationship("Appointment", back_populates="user")
    patient_histories = relationship("PatientHistory", back_populates="user")
