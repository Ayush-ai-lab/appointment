from sqlalchemy import Column, Integer, String, ForeignKey, DateTime 
from core.database import Base 
from datetime import datetime
class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    number = Column(Integer)
    password = Column(String)
    age = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow(),onupdate=datetime)