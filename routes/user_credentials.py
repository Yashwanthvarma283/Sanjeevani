from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates=Jinja2Templates(directory="templates")

router=APIRouter()

@router.get("/")
def landing_page(request:Request):
    return templates.TemplateResponse("index.html",{
        "request":request
    })


@router.get("/user/login")
def login_page(request:Request):
    return "from login page"