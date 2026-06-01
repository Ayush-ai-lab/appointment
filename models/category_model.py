from core.database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime  , ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship
class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey("department.id"))
    slug = Column(String)
    short_description = Column(String)
    description = Column(Text)
    status = Column(String)
    created_by = Column(String)
    updated_by = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    appointments = relationship("Appointment", back_populates="category")
    department = relationship("Department", back_populates="categories")
    doctors = relationship("Doctor", back_populates="category")

