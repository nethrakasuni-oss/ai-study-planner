from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
import app.models as models
import app.schemas as schemas
from app.models import User
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Study Planner API")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "AI Study Planner API is running"}


@app.post("/users")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()