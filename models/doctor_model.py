from core.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from datetime import datetime
from sqlalchemy.orm import relationship
class Doctor(Base):
    __tablename__ = "doctor"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    number = Column(Integer)
    experience = Column(Integer)
    qualification = Column(String)
    bio = Column(Text)
    created_by = Column(String)
    updated_by = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship("Category", back_populates="doctors")
    appointments = relationship("Appointment", back_populates="doctor")
    availabilities = relationship("DoctorAvailability", back_populates="doctor")
    leaves = relationship("Leave", back_populates="doctor")
    slots = relationship("Slot", back_populates="doctor")
    patient_histories = relationship("PatientHistory", back_populates="doctor")
