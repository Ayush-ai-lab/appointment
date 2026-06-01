from core.database import Base 
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from datetime import datetime

class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    country = Column(String)
    state = Column(String)
    city = Column(String)
    street_address = Column(String)
    address = Column(String)
    pin_code = Column(Integer)
    created_by = Column(String)
    updated_by = Column(String) 
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status = Column(String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="address")
    
