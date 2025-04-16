# api/index.py
from mangum import Mangum
from app.main import app  # Keep using your original main.py

handler = Mangum(app)
