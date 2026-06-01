from core.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from datetime import datetime
from sqlalchemy.orm import relationship


class PatientHistory(Base):
    __tablename__ = "patient_history"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    email = Column(String)
    mobile_number = Column(String)
    registration_number = Column(String)
    doctor_id = Column(Integer, ForeignKey("doctor.id"), nullable=False)
    appointment_id = Column(Integer, ForeignKey("appointment.id"), nullable=False)
    symptoms = Column(Text)
    diagnosis = Column(Text)
    prescription = Column(Text)
    created_by = Column(String)
    updated_by = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="patient_histories")
    doctor = relationship("Doctor", back_populates="patient_histories")
    appointment = relationship("Appointment", back_populates="patient_history")
