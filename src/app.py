from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import Response
from sqlalchemy.orm import Session
from src.database import SessionLocal, engine
from src import models, schemas, crud
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Event Management Service", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to the Event Management API"}


@app.post("/events", response_model=dict, status_code=status.HTTP_201_CREATED, tags=["Events"])
def create_event_endpoint(
    event: schemas.EventCreate, 
    response: Response,  # Add response to modify headers
    db: Session = Depends(get_db)
):
    created_event = crud.create_event(db, event)
    # Set the Link header pointing to the newly created resource
    response.headers["Link"] = f"</events/{created_event['id']}>; rel=\"self\""
    return created_event


@app.get("/events", response_model=list, tags=["Events"])
def get_events_endpoint(db: Session = Depends(get_db)):
    return crud.get_all_events(db)


@app.get("/events/{id}", response_model=dict, tags=["Events"])
def get_event_by_id_endpoint(id: int, db: Session = Depends(get_db)):
    event = crud.get_event_by_id(db, id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@app.put("/events/{id}", response_model=dict, tags=["Events"])
def update_event_endpoint(id: int, event: schemas.EventUpdate, db: Session = Depends(get_db)):
    updated_event = crud.update_event(db, id, event)
    if not updated_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event


@app.delete("/events/{id}", response_model=dict, tags=["Events"])
def delete_event_endpoint(id: int, db: Session = Depends(get_db)):
    deleted_event = crud.delete_event(db, id)
    if not deleted_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return deleted_event
