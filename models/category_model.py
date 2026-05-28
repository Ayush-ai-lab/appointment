from core.database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    short_description = Column(String)
    description = Column(Text)
    status = Column(String)
    created_by = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
     

