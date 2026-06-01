from sqlalchemy import Column, String,Integer, ForeignKey, DateTime
from core.database import Base 
from datetime import datetime
from sqlalchemy.orm import relationship
class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key= True)
    name = Column(String)
    slug = Column(String)
    icon = Column(String)
    image = Column(String)
    status = Column(String)
    created_by = Column(String)
    updated_by = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    appointments = relationship("Appointment",back_populates="department")
    categories = relationship("Category", back_populates="department")
