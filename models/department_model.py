from sqlalchemy import Column, String,Integer, ForeignKey, DateTime
from core.database import Base 
from datetime import datetime
class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key= True)
    name = Column(String)
    slug = Column(String)
    icon = Column(String)
    image = Column(String)
    status = Column(String)
    created_by = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)