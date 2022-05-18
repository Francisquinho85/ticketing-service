from sqlalchemy import Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship

from database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)
    date = Column(String)
    number_tickets = Column(Integer)
    ticket_price = Column(Numeric(10,2))
    promotor = Column(String)
    description = Column(String)

    events = relationship("Ticket", back_populates="tickets")

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    nif = Column(Integer, unique=True)
    status = Column(Integer)
    name = Column(String)

    tickets = relationship("Event", back_populates="events")