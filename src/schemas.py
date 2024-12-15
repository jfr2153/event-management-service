# src/schemas.py

from typing import Optional
from pydantic import BaseModel

class EventBase(BaseModel):
    organizationId: int
    name: str
    description: str
    date: str
    time: str
    location: str
    category: str
    rsvpCount: int = 0

class EventCreate(EventBase):
    pass

class EventUpdate(BaseModel):
    organizationId: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None
    time: Optional[str] = None
    location: Optional[str] = None
    category: Optional[str] = None
    rsvpCount: Optional[int] = None

class Event(EventBase):
    id: int

    class Config:
        from_attributes = True
