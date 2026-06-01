from core.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Time, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship


class DoctorAvailability(Base):
    __tablename__ = "doctor_availability"

    id = Column(Integer, primary_key=True)
    created_by = Column(String)
    updated_by = Column(String)
    status = Column(String)
    doctor_id = Column(Integer, ForeignKey("doctor.id"), nullable=False)
    day_of_week = Column(String)  # Monday, Tuesday, etc.
    start_time = Column(Time)
    end_time = Column(Time)
    slot_interval = Column(Integer)  # in minutes
    break_start = Column(Time, nullable=True)
    break_end = Column(Time, nullable=True)
    leave_id = Column(Integer, ForeignKey("leave.id"), nullable=True)
    specific_date = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    doctor = relationship("Doctor", back_populates="availabilities")
    leave = relationship("Leave", back_populates="availabilities")
