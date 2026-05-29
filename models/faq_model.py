from core.database import Base 
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

class Faq(Base):
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime, onupdate=datetime.utcnow())