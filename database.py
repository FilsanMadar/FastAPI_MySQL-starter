from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the URL for the MySQL database
# Replace "springstudent:springstudent" with the appropriate username and password
URL_DATABASE = "mysql+pymysql://springstudent:springstudent@127.0.0.1:3306/BlogApplication"

# Create an engine to connect to the MySQL database
engine = create_engine(URL_DATABASE)

# Create a sessionmaker object to create sessions bound to the engine
# Sessions will be used to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a declarative base class for database models
# All database models will inherit from this base class
Base = declarative_base()


