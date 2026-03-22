from pydantic import BaseModel
from typing import Optional

class EventCreate(BaseModel):
    title: str
    description: str
    location: str
    event_date: str
    capacity: int

class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    event_date: Optional[str] = None
    capacity: Optional[int] = None

class EventResponse(BaseModel):
    id: int
    title: str
    description: str
    location: str
    event_date: str
    capacity: int

    class Config:
        from_attributes = True
