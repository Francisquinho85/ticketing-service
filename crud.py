from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import models, schemas

def get_event_by_id(db: Session, event_id: int):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Event with id {event_id} was not found')
    return event

def get_events(db: Session, skip: int = 0, limit: int = 100):
    events = db.query(models.Event).offset(skip).limit(limit).all()
    if not events:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No event found')
    return events

def create_event(db: Session, event: schemas.Event):
    db_event = models.Event(name=event.name, location=event.location, date=event.date, number_tickets=event.number_tickets, ticket_price=event.ticket_price, promotor=event.promotor, description=event.description)
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    create_tickets(db, db_event.id, db_event.number_tickets)
    return db_event

def update_event(db: Session, event: schemas.UpdateEvent, event_id: int):
    update_event = db.query(models.Event).filter(models.Event.id == event_id)
    if not update_event.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Event with id {event_id} was not found')
    
    if event.name:
        update_event.update({"name": event.name})
    if event.location:
        update_event.update({"location": event.location})
    if event.date:
        update_event.update({"date": event.date})
    if event.ticket_price:
        update_event.update({"ticket_price": event.ticket_price})
    if event.number_tickets:
        update_event.update({"number_tickets": event.number_tickets})
    if event.promotor:
        update_event.update({"promotor": event.promotor})
    if event.description:
        update_event.update({"description": event.description})
    db.commit()
    return update_event.first()

def delete_event(db: Session, event_id: int):
    deleted_event = db.query(models.Event).filter(models.Event.id == event_id)
    i = 0

    while i < deleted_event.n_tickets:
        delete_ticket(event_id)
        i += 1

    if not deleted_event.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Event with id {event_id} was not found')
    deleted_event.delete(synchronize_session=False)
    db.commit()
    return {"Success": f"Event with id {event_id} was successfully deleted"}

def get_ticket_by_id(db: Session, ticket_id: int):
    ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()
    if not ticket:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Ticket with id {ticket} was not found')
    return ticket

def get_tickets(db: Session,  nif: int, status: int, name: str, event_id: int, skip: int = 0, limit: int = 100):
    tickets = db.query(models.Ticket)
    if nif != None:
        tickets = tickets.filter(models.Ticket.nif == nif)
    if status != None:
        tickets = tickets.filter(models.Ticket.status == status)
    if name != None:
        tickets = tickets.filter(models.Ticket.name == name)
    if event_id != None:
        tickets = tickets.filter(models.Ticket.event_id == event_id)
    if not tickets:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'No ticket found')
    return tickets.offset(skip).limit(limit).all()

def create_tickets(db: Session, event_id: int, n_tickets: int):
    i = 0
    while i < n_tickets:
        create_ticket(db, event_id)
        i += 1
    return 0

def create_ticket(db: Session, e_id: int):
    db_ticket = models.Ticket(nif=None, status=0, name=None, event_id=e_id)
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def update_ticket(db: Session, ticket: schemas.UpdateTicket, ticket_id: int):
    update_ticket = db.query(models.Ticket).filter(models.Ticket.id == ticket_id)
    if not update_ticket.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Ticket with id {ticket_id} was not found')
    
    if ticket.nif:
        update_ticket.update({"nif": ticket.nif})
    if ticket.status:
        update_ticket.update({"status": ticket.status})
    if ticket.name:
        update_ticket.update({"name": ticket.name})
    db.commit()
    return update_ticket.first()

def delete_ticket(db: Session, event_id: int):
    deleted_ticket = db.query(models.Ticket).filter(models.Ticket.event_id == event_id).first()

    if not deleted_ticket.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Ticket with id {deleted_ticket.id} was not found')
    deleted_ticket.delete(synchronize_session=False)
    db.commit()
    return {"Success": f"Ticket with id {deleted_ticket.id} was successfully deleted"}