from fastapi import APIRouter, Request,Depends
from fastapi.templating import Jinja2Templates
from services.user_service import create_user,get_users
from schemas.user_schema import userCreation,userResponse
from sqlalchemy.orm import Session
from database.db import SessionLocal

def get_db(): #default usage
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

templates=Jinja2Templates(directory="templates")#default usage

router=APIRouter()#default usage

@router.get("/user/dashboard")
def landing_page():
    return "From User Dashboard"

@router.post("/user/creation")
def create(user:userCreation,db:Session=Depends(get_db) ):
    return create_user(db,user.name)


@router.get("/user/response",response_model=list[userResponse])
def read(db:Session=Depends(get_db)):
    return get_users(db)