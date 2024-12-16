# Event Management Service

This is a simple Event Management Service built using FastAPI. The service allows users to create, read, update, and delete events.

## Features

- Create events
- Retrieve all events or a specific event by ID
- Update existing events
- Delete events

## Requirements

- Python 3.7 or higher
- FastAPI
- Uvicorn
- MySQL-Connector-Python (for MySQL database connection)
- python-dotenv (for loading environment variables)

## Installation

1. Clone the repository:

   git clone <repository-url>
   cd event-management-service

2. Create a virtual environment:
    python -m venv venv

3. Activate the virtual environment:

    On macOS/Linux:
    source venv/bin/activate

    On Windows:
    .\venv\Scripts\activate

4. Install the required packages:

    pip install -r requirements.txt

5. Create a .env file in the project root directory with the following content:

    DB_USER=root
    DB_PASSWORD=dbuserdbuser
    DB_HOST=event-management-service.cyswkjclynii.us-east-1.rds.amazonaws.com
    DB_PORT=3306
    DB_NAME=events_db


## Running the Application

1. Ensure your database is set up and accessible.

2. Run the FastAPI application using Uvicorn:

    uvicorn src.app:app --host 0.0.0.0 --port 8001

3. Open your browser and go to http://127.0.0.1:8001 to see the application running.

4. Access the interactive API documentation at http://127.0.0.1:8001/docs.


## API Endpoints

    - GET /: Returns a welcome message.
    - POST /events/: Create a new event.
    - GET /events/: Retrieve a list of all events.
    - GET /events/{event_id}: Retrieve a specific event by ID.
    - PUT /events/{event_id}: Update an existing event by ID.
    - DELETE /events/{event_id}: Delete an event by ID.

## Accessing the Database

1. Open Your Terminal:

2. Connect to Your MySQL Database:

    mysql -h event-management-service.cyswkjclynii.us-east-1.rds.amazonaws.com -P 3306 -u root -p

3. Enter Your Password:

    dbuserdbuser

4. Select Your Database:

    USE events_db;

5. To See Database Contents:

    SELECT * FROM Events;


## Expected Output:

+----+----------------+--------------------+-------------------------------+------------+----------+-------------+-------------+-----------+
| id | organizationId | name               | description                   | date       | time     | location    | category    | rsvpCount |
+----+----------------+--------------------+-------------------------------+------------+----------+-------------+-------------+-----------+
|  1 |              1 | Hackathon 2024     | A technology hackathon event  | 2024-12-15 | 10:00:00 | Campus Hall | Technology  |         0 |
|  2 |              2 | Updated Hackathon  | Updated description           | 2024-12-20 | 12:00:00 | Updated Hall| Tech Update |         5 |
+----+----------------+--------------------+-------------------------------+------------+----------+-------------+-------------+-----------+

6. Exit MySQL:

    EXIT;

Expected Response:

    Bye

## Deployment on AWS EC2

1.    Launch an EC2 Instance:
        - Use the AWS Management Console to launch an EC2 instance.
        - Choose an Amazon Linux 2023 AMI.
        - Select a t2.micro instance (free tier eligible) for testing.
        - Open port 8000 in the EC2 security group to allow inbound traffic.

2. Connect to the Instance:

    ssh -i "/path/to/key.pem" ec2-user@<EC2_PUBLIC_IP>

3. Install Required Packages:

    sudo yum update -y
    sudo yum install -y python3 git
    pip3 install fastapi uvicorn mysql-connector-python python-dotenv

4. Clone the Repository:

    git clone <repository-url>
    cd event-management-service

5. Run the Application:

    uvicorn src.app:app --host 0.0.0.0 --port 8001

6. Access the application:

    http://<EC2_PUBLIC_IP>:8000
    
---

# Event Management API Documentation

## Base URL

- **Local Development**: `http://127.0.0.1:8000`

---

## Middleware

### Logging Middleware

- **Purpose**: Logs all incoming requests and outgoing responses, along with metadata such as request headers, response status codes, and execution time.
- **Details**:
  - Generates a unique request ID for each request to trace logs.
  - Logs request headers and body for debugging.
  - Measures processing time for performance monitoring.

---

## Endpoints

### 1. GET `/`

- **Description**: Returns a welcome message.
- **Response**:
  - **Status Code**: `200 OK`
  - **Body**:
    ```json
    {
      "message": "Welcome to the Event Management API"
    }
    ```

---

### 2. POST `/events`

- **Description**: Creates a new event.
- **Request Body** (JSON):
  ```json
  {
    "organizationId": 1,
    "name": "Event Name",
    "description": "Description of the event",
    "date": "YYYY-MM-DD",
    "time": "HH:MM",
    "location": "Event location",
    "category": "Event category",
    "rsvpCount": 0
  }
  ```
- **Response**:
  - **Status Code**: `201 Created`
  - **Body**: The created event object.
    ```json
    {
      "id": 3,
      "organizationId": 1,
      "name": "Event Name",
      "description": "Description of the event",
      "date": "YYYY-MM-DD",
      "time": "HH:MM",
      "location": "Event location",
      "category": "Event category",
      "rsvpCount": 0
    }
    ```

---

### 3. GET `/events`

- **Description**: Retrieves a list of events with optional filtering by date.
- **Query Parameters**:
  - `date` (string, optional): Filter by event date in `YYYY-MM-DD` format. If not specified, retrieves events from all dates.
  - `page` (integer, default: 1): The current page.
  - `limit` (integer, default: 10): Number of items per page.
- **Response**:
  - **Status Code**: `200 OK`
  - **Body**:
    ```json
    {
      "page": 1,
      "limit": 10,
      "total": 50,
      "events": [
        {
          "id": 3,
          "organizationId": 1,
          "name": "Event Name",
          "description": "Description of the event",
          "date": "YYYY-MM-DD",
          "time": "HH:MM",
          "location": "Event location",
          "category": "Event category",
          "rsvpCount": 0
        },
        ...
      ]
    }
    ```

---

### 4. GET `/events/{id}`

- **Description**: Retrieves an event by its ID.
- **Path Parameters**:
  - `id` (integer): The ID of the event.
- **Response**:
  - **Status Code**: `200 OK` if found.
  - **Status Code**: `404 Not Found` if the event does not exist.
  - **Body**:
    **Example (Found):**
    ```json
    {
      "id": 3,
      "organizationId": 1,
      "name": "Event Name",
      "description": "Description of the event",
      "date": "YYYY-MM-DD",
      "time": "HH:MM",
      "location": "Event location",
      "category": "Event category",
      "rsvpCount": 0
    }
    ```
    **Example (Not Found):**
    ```json
    {
      "detail": "Event not found"
    }
    ```

---

### 5. PUT `/events/{id}`

- **Description**: Updates an existing event.
- **Path Parameters**:
  - `id` (integer): The ID of the event to update.
- **Request Body** (JSON):
  ```json
  {
    "organizationId": 1,
    "name": "Updated Event Name",
    "description": "Updated description",
    "date": "YYYY-MM-DD",
    "time": "HH:MM",
    "location": "Updated location",
    "category": "Updated category",
    "rsvpCount": 10
  }
  ```
- **Response**:
  - **Status Code**: `200 OK` if updated.
  - **Status Code**: `404 Not Found` if the event does not exist.
  - **Body**:
    **Example (Updated):**
    ```json
    {
      "id": 3,
      "organizationId": 1,
      "name": "Updated Event Name",
      "description": "Updated description",
      "date": "YYYY-MM-DD",
      "time": "HH:MM",
      "location": "Updated location",
      "category": "Updated category",
      "rsvpCount": 10
    }
    ```
    **Example (Not Found):**
    ```json
    {
      "detail": "Event not found"
    }
    ```

---

### 6. DELETE `/events/{id}`

- **Description**: Deletes an event.
- **Path Parameters**:
  - `id` (integer): The ID of the event to delete.
- **Response**:
  - **Status Code**: `200 OK` if deleted.
  - **Status Code**: `404 Not Found` if the event does not exist.
  - **Body**:
    **Example (Deleted):**
    ```json
    {
      "message": "Event deleted successfully"
    }
    ```
    **Example (Not Found):**
    ```json
    {
      "detail": "Event not found"
    }
    ```

---

## Models

### Event

- **Fields**:
  - `id` (integer): The unique identifier of the event.
  - `organizationId` (integer): The ID of the organization hosting the event.
  - `name` (string): The name of the event.
  - `description` (string, optional): A description of the event.
  - `date` (string): The date of the event (YYYY-MM-DD).
  - `time` (string): The time of the event.
  - `location` (string): The location of the event.
  - `category` (string): The category of the event.
  - `rsvpCount` (integer): The number of RSVPs.

---

## Error Responses

- **400 Bad Request**: Invalid input or parameters.
- **404 Not Found**: The requested resource could not be found.
- **500 Internal Server Error**: A server error occurred.

---


