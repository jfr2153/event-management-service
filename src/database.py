import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

def create_connection():
    try:
        # Use environment variables to get the connection details
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT"))  # Ensure port is an integer
        )
        
        print("Connected to the database!")
        return connection
    
    except Error as e:
        print(f"Error: {e}")
        return None


db_connection = create_connection()
