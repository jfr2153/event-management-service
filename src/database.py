import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="event-management-service.cyswkjclynii.us-east-1.rds.amazonaws.com",
            user="root",
            password="dbuserdbuser",
            database="events_db",
            port=3306
        )
        print("Connected to the database!")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

db_connection = create_connection()
