from sqlalchemy import String, Column, Integer, ForeignKey, DateTime, Time
from core.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Slot(Base):
    __tablename__ = "slot"

    id = Column(Integer, primary_key=True)
    created_by = Column(String)
    updated_by = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    doctor_id = Column(Integer, ForeignKey("doctor.id"))
    slot_start = Column(Time)
    slot_end = Column(Time)
    slot_date = Column(String)
    doctor = relationship("Doctor", back_populates="slots")
    appointments = relationship("Appointment", back_populates="slot")
