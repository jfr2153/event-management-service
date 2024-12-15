from sqlalchemy.orm import Session
from src.models import Event
from src.schemas import EventCreate, EventUpdate

def add_hateoas_to_event(event: dict):
    return {
        **event,
        "_links": {
            "self": f"/events/{event['id']}",
            "update": f"/events/{event['id']}",
            "delete": f"/events/{event['id']}",
            "organization": f"/organizations/{event['organizationId']}"
        }
    }

def sqlalchemy_to_dict(obj):
    return {c.key: getattr(obj, c.key) for c in obj.__table__.columns}

def create_event(db: Session, event: EventCreate):
    db_event = Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)  # auto-generated ID
    return add_hateoas_to_event(sqlalchemy_to_dict(db_event)) #HATEOAS links

def get_all_events(db: Session):
    events = db.query(Event).all()
    return [add_hateoas_to_event(sqlalchemy_to_dict(event)) for event in events] #HATEOAS links

def get_event_by_id(db: Session, event_id: int):
    event = db.query(Event).filter(Event.id == event_id).first()
    return add_hateoas_to_event(sqlalchemy_to_dict(event)) if event else None #HATEOAS links

def update_event(db: Session, event_id: int, event_update: EventUpdate):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if db_event:
        for key, value in event_update.dict(exclude_unset=True).items():
            setattr(db_event, key, value)
        db.commit()
        db.refresh(db_event)
        return add_hateoas_to_event(sqlalchemy_to_dict(db_event)) #HATEOAS links
    return None

def delete_event(db: Session, event_id: int):
    db_event = db.query(Event).filter(Event.id == event_id).first()
    if db_event:
        db.delete(db_event)
        db.commit()
        return {
            "message": "Event deleted successfully",
            "_links": {
                "create": "/events", #HATEOAS link to create event
                "all": "/events" #HATEOAS link to read all events
            }
        }
    return None
