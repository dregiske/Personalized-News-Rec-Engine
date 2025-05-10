from sqlalchemy.orm import Session
from app import models

def get_users(db: Session | None = None):
    if db is None:
        from app.database import SessionLocal
        db = SessionLocal()
    try:
        return db.query(models.User).all()
    finally:
        db.close()
