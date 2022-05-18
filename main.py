#run this program with python3 -m uvicorn main:app --reload on Windows
#or just uvicorn main:app --reload on Linux

from fastapi import Depends, FastAPI
from fastapi_versioning import VersionedFastAPI, version
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import crud, models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/event/{event_id}", response_model=schemas.Event)
@version(1)
def get_event_by_id(event_id: int, db: Session = Depends(get_db)):
    return crud.get_event_by_id(db, event_id)

@app.get("/events/", response_model=list[schemas.Event])
@version(1)
def get_events(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_events(db, skip, limit)

@app.post("/event/", response_model=schemas.Event)
@version(1)
def create_event(event: schemas.Event, db: Session = Depends(get_db)):
    return crud.create_event(db, event)

@app.put("/event/{event_id}")
@version(1)
def update_event(event_id: int, event: schemas.UpdateEvent, db: Session = Depends(get_db)):
    return crud.update_event(db, event, event_id)

@app.delete("/event/{event_id}")
@version(1)
def delete_event(event_id: int, db: Session = Depends(get_db)):
    return crud.delete_event(db, event_id)

@app.post("/ticket/")
@version(1)
def create_ticket(ticket: schemas.Ticket, db: Session = Depends(get_db)):
    return crud.create_ticket(db, ticket)

@app.get("/ticket/{ticket_id}")
@version(1)
def get_ticket_by_id(ticket_id: int, db: Session = Depends(get_db)):
    return crud.get_ticket_by_id(db, ticket_id)

@app.get("/tickets/")
@version(1)
def get_tickets(nif: int = None, status: int = None, name: str = None, event_id: int = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_tickets(db, nif, status, name, event_id, skip, limit)

@app.put("/ticket/{ticket_id}")
@version(1)
def update_ticket(ticket_id: int, ticket: schemas.UpdateTicket, db: Session = Depends(get_db)):
    return crud.update_ticket(db, ticket, ticket_id)

@app.post("/ticket/{ticket_id}/pay/")
@version(1)
def pay_ticket(ticket_id: int):
    #paymentService.pay(ticket_id, amount, nif)
    return {"Success": "Ticket paid successfully"}

app = VersionedFastAPI(app,
    version_format='{major}',
    prefix_format='/v{major}')