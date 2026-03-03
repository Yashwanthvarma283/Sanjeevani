from fastapi import FastAPI
from routes import user_credentials, User_routings
from database.db import engine, Base
from models import user

app = FastAPI()

app.include_router(user_credentials.router)
app.include_router(User_routings.router)
Base.metadata.create_all(bind=engine)