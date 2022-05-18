from pydantic import BaseModel
from typing import Optional

class Event(BaseModel):
    name: str
    location: str
    date: str
    number_tickets: int
    ticket_price: float
    promotor: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True

class UpdateEvent(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    date: Optional[str] = None
    number_tickets: Optional[int] = None
    ticket_price: Optional[float] = None
    promotor: Optional[str] = None
    description: Optional[str] = None

class Ticket(BaseModel):
    nif: Optional[int] = None
    status: Optional[int] = None
    name: Optional[str] = None
    event_id: int

    class Config:
        orm_mode = True

class UpdateTicket(BaseModel):
    nif: Optional[int] = None
    status: Optional[int] = 0
    name: Optional[str] = None