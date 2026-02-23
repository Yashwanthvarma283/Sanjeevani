from fastapi import FastAPI
from routes.user_credentials import router

app = FastAPI()

app.include_router(router)