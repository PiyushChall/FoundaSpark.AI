from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./users.db"

# Setup SQLAlchemy Engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Session local for getting db session in each request
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for getting database session in routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
