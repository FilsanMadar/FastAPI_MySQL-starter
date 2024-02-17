# what sqlalchemy (orm) uses to be able to create the tables that we need in mysql database

from sqlalchemy import Boolean, Column, Integer, String
from database import Base

class User(Base):
    # Set the table name for the User model
    __tablename__ = 'users'

    # Define columns for the User model
    # Primary key column 'id' for unique identification
    id = Column(Integer, primary_key=True, index=True)

    # Username column with a maximum length of 50 characters and should be unique
    username = Column(String(50), unique=True)

# Define a SQLAlchemy model for posts
class Post(Base):
    # Set the table name for the Post model
    __tablename__ = 'posts'

    # Define columns for the Post model
    # Primary key column 'id' for unique identification
    id = Column(Integer, primary_key=True, index=True)

    # Title column with a maximum length of 50 characters
    title = Column(String(50))

    # Content column with a maximum length of 100 characters
    content = Column(String(100))

    # ForeignKey column 'user_id' to establish a relationship with the User model
    user_id = Column(Integer)