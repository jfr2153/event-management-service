# src/models.py

from sqlalchemy import Column, Integer, String, Text
from src.database import Base

class Event(Base):
    __tablename__ = "Events"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    organizationId = Column(Integer, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    date = Column(String(50), nullable=False)
    time = Column(String(50), nullable=False)
    location = Column(String(255), nullable=False)
    category = Column(String(255), nullable=False)
    rsvpCount = Column(Integer, default=0)
