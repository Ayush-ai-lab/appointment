from core.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
class Doctor(Base):
    __tablename__ = "doctor"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    number = Column(Integer)
    experience = Column(Integer)
    qualification = Column(String)
    bio = Column(Text)
    create_by = Column(String)
    updated_by = Column(String)
    created_at = Column(default=datetime.utcnow())
    updated_at = Column(default=datetime.utcnow(), onupdate=datetime.utcnow())