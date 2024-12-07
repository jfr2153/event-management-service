from src.database import db_connection
from typing import Optional

# Create Event
def create_event(event):
    cursor = db_connection.cursor()
    query = """
    INSERT INTO Events (organizationId, name, description, date, time, location, category, rsvpCount)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        event.organizationId,
        event.name,
        event.description,
        event.date,
        event.time,
        event.location,
        event.category,
        event.rsvpCount,
    )
    cursor.execute(query, values)
    db_connection.commit()
    return {"id": cursor.lastrowid, **event.dict()}

def get_all_events(page: int, limit: int, date: Optional[str] = None):
    cursor = db_connection.cursor(dictionary=True)
    
    offset = (page - 1) * limit
    
    query = "SELECT * FROM Events"
    values = []
    
    if date:
        query += " WHERE date = %s"
        values.append(date)
    
    query += " LIMIT %s OFFSET %s"
    values.extend([limit, offset])
    
    cursor.execute(query, tuple(values))
    events = cursor.fetchall()
    
    count_query = "SELECT COUNT(*) AS total FROM Events"
    if date:
        count_query += " WHERE date = %s"
        cursor.execute(count_query, (date,))
    else:
        cursor.execute(count_query)
    
    total_count = cursor.fetchone()['total']
    
    return {
        "page": page,
        "limit": limit,
        "total": total_count,
        "events": events
    }

# Get Event by ID
def get_event_by_id(event_id):
    cursor = db_connection.cursor(dictionary=True)
    query = "SELECT * FROM Events WHERE id = %s"
    cursor.execute(query, (event_id,))
    return cursor.fetchone()

# Update Event
def update_event(event_id, event):
    cursor = db_connection.cursor()
    query = """
    UPDATE Events
    SET organizationId = %s, name = %s, description = %s, date = %s, time = %s, location = %s, category = %s, rsvpCount = %s
    WHERE id = %s
    """
    values = (
        event.organizationId,
        event.name,
        event.description,
        event.date,
        event.time,
        event.location,
        event.category,
        event.rsvpCount,
        event_id,
    )
    cursor.execute(query, values)
    db_connection.commit()
    return {"id": event_id, **event.dict()}

# Delete Event
def delete_event(event_id):
    cursor = db_connection.cursor()
    query = "DELETE FROM Events WHERE id = %s"
    cursor.execute(query, (event_id,))
    db_connection.commit()
    return {"message": "Event deleted successfully"}