from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import Field
import os

SQLALCHEMY_DATABASE_URL = ""
#SQLALCHEMY_DATABASE_URL = "postgresql://francisco:ticketing@db-ticketing:5432/ticketingdb"
with open("/tmp/secrets/ticketing-secret", 'r') as f:
    SQLALCHEMY_DATABASE_URL = f.read().strip()

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()