from core.database import Base
from sqlalchemy import Column, ForeignKey, Integer, Date, String, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship


class Leave(Base):
    __tablename__ = "leave"

    id = Column(Integer, primary_key=True)
    created_by = Column(String)
    updated_by = Column(String)
    status = Column(String)
    doctor_id = Column(Integer, ForeignKey("doctor.id"))
    specific_date = Column(Date)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    doctor = relationship("Doctor", back_populates="leaves")
    availabilities = relationship("DoctorAvailability", back_populates="leave")
