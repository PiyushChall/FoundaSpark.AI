from passlib.hash import bcrypt
from sqlalchemy.orm import Session
from models import User  # Import User model from models.py
from database import get_db

# Function to authenticate the user during login
def authenticate_user(username: str, password: str, db: Session) -> bool:
    user = db.query(User).filter(User.username == username).first()
    if user and bcrypt.verify(password, user.password):
        return True
    return False

# Function to register a new user
def register_user(username: str, password: str, db: Session):
    if db.query(User).filter(User.username == username).first():
        raise ValueError("Username already taken")
    hashed_password = bcrypt.hash(password)
    user = User(username=username, password=hashed_password)
    db.add(user)
    db.commit()

# Function to check if a username already exists
def username_exists(username: str, db: Session) -> bool:
    return db.query(User).filter(User.username == username).first() is not None
