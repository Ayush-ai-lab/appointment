from datetime import datetime

from core.database import Base
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship


class Meeting(Base):
    __tablename__ = "meeting"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    created_by = Column(String)
    updated_by = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    appointments = relationship("Appointment", back_populates="meeting")
