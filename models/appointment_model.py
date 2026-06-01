from core.database import Base 
from sqlalchemy import Column, String, Integer, ForeignKey,DateTime, Text
from datetime import datetime
from sqlalchemy.orm import relationship
class Appointment(Base):
    __tablename__ = "appointment"

    id = Column(Integer, primary_key=True)
    created_by = Column(String)
    updated_by = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = Column(String)
    department_id = Column(Integer, ForeignKey("department.id"), nullable=False)
    user_id = Column(Integer,ForeignKey("user.id"),nullable=False)
    category_id = Column(Integer,ForeignKey("category.id"),nullable=False)
    doctor_id =  Column(Integer, ForeignKey("doctor.id"), nullable=True)
    short_description = Column(String)
    appointment_date = Column(DateTime)
    appointment_status = Column(Integer)
    payment_status = Column(Integer)
    notes = Column(Text)
    symptoms =  Column(Text)
    slot_id = Column(Integer,ForeignKey("slot.id"), nullable=True)
    appointment_valid_date = Column(DateTime)
    prescription = Column(Text)
    meeting_id = Column(Integer, ForeignKey("meeting.id"), nullable=True)
    weight = Column(Integer)
    bp = Column(String)

    department = relationship("Department", back_populates="appointments")
    category = relationship("Category", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")
    user = relationship("User", back_populates="appointments")
    slot = relationship("Slot", back_populates="appointments")
    meeting = relationship("Meeting", back_populates="appointments")
    patient_history = relationship("PatientHistory", back_populates="appointment")
