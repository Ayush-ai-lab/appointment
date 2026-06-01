from core.database import Base 
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

class Faq(Base):
    __tablename__ = "faq"
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(Text)
    status = Column(Integer)
    created_by = Column(String)
    updated_by = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
