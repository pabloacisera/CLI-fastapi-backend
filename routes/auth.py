from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from helpers.dependencies import get_db
from schemas import UserResponseRegister, UserResponseLogin, UserCreate, UserLogin
from controllers import AuthController


AuthRouter = APIRouter(prefix="/api/auth", tags=["auth"])

@AuthRouter.post("/register", response_model=UserResponseRegister)
def register(user: UserCreate, db: Session = Depends(get_db)):
    return AuthController.register(user, db)

@AuthRouter.post("/login", response_model=UserResponseLogin)
def login(user: UserLogin, db: Session = Depends(get_db)):
    return AuthController.login(user, db)
