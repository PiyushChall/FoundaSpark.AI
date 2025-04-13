from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from passlib.hash import bcrypt
from sqlalchemy.orm import Session
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles

from llm import analyze_idea_with_ai, analyze_market_research

from database import get_db, engine
import models
from auth import authenticate_user, register_user, username_exists


app = FastAPI()

# Mounting the static files for CSS, images, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Middleware for handling sessions
app.add_middleware(SessionMiddleware, secret_key="supersecretkey")

templates = Jinja2Templates(directory="templates")

# Create the database tables at startup
@app.on_event("startup")
def on_startup():
    # This will create tables if they don't exist
    models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root(request: Request):
    user = request.session.get("user")
    if user:
        return templates.TemplateResponse("home.html", {"request": request, "user": user})
    return RedirectResponse("/login", status_code=302)

@app.get("/login")
def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login_post(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    if authenticate_user(username, password, db):
        request.session["user"] = username
        return RedirectResponse("/", status_code=302)
    return templates.TemplateResponse("login.html", {"request": request, "error": "Invalid credentials"})

@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/login", status_code=302)

@app.get("/register")
def register_get(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register")
def register_post(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    try:
        register_user(username, password, db)
        request.session["user"] = username
        return RedirectResponse("/", status_code=302)
    except ValueError as e:
        return templates.TemplateResponse("register.html", {"request": request, "error": str(e)})


@app.post("/analyze_idea")
def analyze_idea_post(request: Request, idea: str = Form(...)):
    print(f"Received idea: {idea}")

    user = request.session.get("user")
    if not user:
        return RedirectResponse("/login", status_code=302)

    analysis_result = analyze_idea_with_ai(idea)
    return templates.TemplateResponse("idea_analysis.html", {
        "request": request,
        "analysis_result": analysis_result
    })

@app.post("/market_research")
def market_research_post(request: Request, idea: str = Form(...)):
    """
    Endpoint to analyze market research for a given startup idea.
    """
    print(f"Received idea for market research: {idea}")
    user = request.session.get("user")
    if not user:
        return RedirectResponse("/login", status_code=302)

    # Call the analyze_market_research function
    analysis_result = analyze_market_research(idea)
    return templates.TemplateResponse("market_research_analysis.html", {
        "request": request,
        "analysis_result": analysis_result
    })