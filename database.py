from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import Field
import os


# POSTGRES_USER = str(Field(..., env='POSTGRES_USER'))
# POSTGRES_PASSWORD = str(Field(..., env='POSTGRES_PASSWORD'))
# POSTGRES_SERVER = str(Field(..., env='POSTGRES_SERVER'))
#POSTGRES_PORT = str(Field(..., env='POSTGRES_PORT'))
# POSTGRES_DB = str(Field(..., env='POSTGRES_DB'))

#SQLALCHEMY_DATABASE_URL = "postgresql://" + POSTGRES_USER + ":" + POSTGRES_PASSWORD + "@" + POSTGRES_SERVER + ":5432/" + POSTGRES_DB
SQLALCHEMY_DATABASE_URL = "postgresql://francisco:ticketing@db-ticketing:5432/ticketingdb"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()