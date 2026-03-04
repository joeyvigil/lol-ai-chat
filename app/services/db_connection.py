from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "sqlite:///./app.db" # DB will live in the app directory


engine = create_engine(
    DB_URL,
    connect_args={"check_same_thread":False} # allows concurrent requests (DB requests at the same time)
)

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = LocalSession() # Create a new session instance
    try:
        yield db # yield? this just means we're sending the DB to the caller indefinitely
    # TODO: could have an except block to catch any kinds of DB-related exceptions
    finally:
        db.close() # Close the connection when done, prevent memory leaks

Base = declarative_base()