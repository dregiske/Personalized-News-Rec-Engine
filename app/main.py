from fastapi import FastAPI
from app import database, models
from app.crud import get_users
from app.schemas import UserOut

# ensure that metadata is created (if you ever call Base.metadata.create_all)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="News Rec Engine")

@app.get("/", tags=["Health"])
def read_root():
    return {"status": "ok", "message": "Welcome to News Rec Engine"}

@app.get("/users/", response_model=list[UserOut], tags=["Users"])
def list_users():
    return get_users()
