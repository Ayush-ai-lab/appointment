from core.database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    message = Column(Text)
    created_by = Column(String)
    created_at = Column(datetime, default=datetime.utcnow())
    updated_at = Column(datetime, default=datetime.utcnow(), onupdate=datetime.utcnow())