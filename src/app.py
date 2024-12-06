from fastapi import FastAPI, HTTPException
from src.models import Event
from src.crud import create_event, get_all_events, get_event_by_id, update_event, delete_event

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the Event Management API"}

@app.post("/events")
def create_event_endpoint(event: Event):
    return create_event(event)

@app.get("/events")
def get_events_endpoint():
    return get_all_events()

@app.get("/events/{id}")
def get_event_by_id_endpoint(id: int):
    event = get_event_by_id(id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@app.put("/events/{id}")
def update_event_endpoint(id: int, event: Event):
    return update_event(id, event)

@app.delete("/events/{id}")
def delete_event_endpoint(id: int):
    return delete_event(id)

#test comment