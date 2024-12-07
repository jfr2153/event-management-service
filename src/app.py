import time
import uuid
from fastapi import FastAPI, Request, HTTPException, Query
from starlette.middleware.base import BaseHTTPMiddleware
from src.models import Event
from src.crud import create_event, get_all_events, get_event_by_id, update_event, delete_event
from datetime import datetime
from typing import Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        request_id = uuid.uuid4()
        request_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        logger.info(f"[{request_id}] Request received at {request_time}: {request.method} {request.url.path}")

        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time

        response_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        logger.info(
            f"[{request_id}] Response completed at {response_time}: "
            f"Status {response.status_code} {request.url.path}, "
            f"Processing time: {process_time:.2f} seconds"
        )
        return response

app = FastAPI()
app.add_middleware(LoggingMiddleware)

@app.get("/")
def root():
    return {"message": "Welcome to the Event Management API"}

@app.post("/events")
def create_event_endpoint(event: Event):
    return create_event(event)

@app.get("/events")
def get_events_endpoint(
    date: Optional[str] = Query(None, description="Filter by Event Date (YYYY-MM-DD)"),
    page: int = Query(1, ge=1, description="Page Number"),
    limit: int = Query(10, ge=1, description="Number of Items per Page")
):
    return get_all_events(page, limit, date)

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