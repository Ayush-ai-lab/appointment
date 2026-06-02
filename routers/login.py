from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from services.login_service import login_user
from core.database import get_db
from schemas.login import LoginSchema
from core.auth import get_current_user
routers = APIRouter(prefix="/login", tags=["login"])

@routers.post("/login")
def login(
    data: LoginSchema,
    db: Session = Depends(get_db)
):
    return login_user(data, db)


@routers.get("/profile")
def profile(
    current_user=Depends(get_current_user)
):
    return current_user