# src/app.py
from kafka import KafkaProducer
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.models import Event
from src.crud import create_event, get_all_events, get_event_by_id, update_event, delete_event
import json

app = FastAPI(title="EVENTS", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def publish_event(topic, event_data):
    producer.send(topic, event_data)
    producer.flush()

@app.get("/")
def root():
    return {"message": "Welcome to Yara's Event Management API"}

@app.post("/events")
def create_event_endpoint(event: Event):
    publish_event("events_topic", {"action": "create", "event": event.dict()})
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
    updated_event = update_event(id, event)
    publish_event("events_topic", {"action": "update", "event": updated_event})
    return update_event(id, event)

@app.delete("/events/{id}")
def delete_event_endpoint(id: int):
    publish_event("events_topic", {"action": "delete", "event_id": id})
    return delete_event(id)

