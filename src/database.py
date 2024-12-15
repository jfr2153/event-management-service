# src/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base  # Import declarative_base
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "dbuserdbuser")
DB_HOST = os.getenv("DB_HOST", "event-management-service.cyswkjclynii.us-east-1.rds.amazonaws.com")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "events_db")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for SQLAlchemy models
Base = declarative_base()  # Fixed import
