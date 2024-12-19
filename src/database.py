#src/database.py
from mysql.connector import pooling, Error

def create_connection_pool():
    try:
        pool = pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=10,
            pool_reset_session=True,
            host="event-management-service.cyswkjclynii.us-east-1.rds.amazonaws.com",
            user="root",
            password="dbuserdbuser",
            database="events_db",
            port=3306
        )
        print("Connection pool created successfully!")
        return pool
    except Error as e:
        print(f"Error creating connection pool: {e}")
        raise e

connection_pool = create_connection_pool()

def get_connection():
    return connection_pool.get_connection()

# import mysql.connector
# from mysql.connector import Error

# def create_connection():
#     try:
#         connection = mysql.connector.connect(
#             host="event-management-service.cyswkjclynii.us-east-1.rds.amazonaws.com",
#             user="root",
#             password="dbuserdbuser",
#             database="events_db",
#             port=3306
#         )
#         print("Connected to the database!")
#         return connection
#     except Error as e:
#         print(f"Error: {e}")
#         return None

# db_connection = create_connection()

# import mysql.connector
# from mysql.connector import Error
# from dotenv import load_dotenv
# import os

# load_dotenv()

# def create_connection():
#     try:
#         # Use environment variables to get the connection details
#         connection = mysql.connector.connect(
#             host=os.getenv("DB_HOST"),
#             user=os.getenv("DB_USER"),
#             password=os.getenv("DB_PASSWORD"),
#             database=os.getenv("DB_NAME"),
#             port=int(os.getenv("DB_PORT"))  # Ensure port is an integer
#         )
        
#         print("Connected to the database!")
#         return connection
    
#     except Error as e:
#         print(f"Error: {e}")
#         return None


# db_connection = create_connection()
