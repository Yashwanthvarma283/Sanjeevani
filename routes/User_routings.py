from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates=Jinja2Templates(directory="templates")

router=APIRouter()

@router.get("/user/dashboard")
def landing_page():
    return "From User Dashboard"