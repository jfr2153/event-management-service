from pydantic import BaseModel

class Event(BaseModel):
    id: int = None
    organizationId: int
    name: str
    description: str
    date: str
    time: str
    location: str
    category: str
    rsvpCount: int = 0
