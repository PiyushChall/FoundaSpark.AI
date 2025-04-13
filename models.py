from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# Base class for all models
Base = declarative_base()

# User table for authentication
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

# Idea table for startup ideas
class Idea(Base):
    __tablename__ = "ideas"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
