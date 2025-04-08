from enum import Enum
from pydantic import BaseModel, EmailStr

class Role(str, Enum):
    USER = "USER"
    ADMIN = "ADMIN"
    GUEST = "GUEST"

class UserBase(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    role: Role

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserCreate(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str
    role: Role = Role.USER

class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Schema para respuesta de registro
class RegisterResponse(BaseModel):
    message: str = "User registered successfully"
    user: UserBase  # Usa el modelo base compartido

# Schema para respuesta de login
class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserBase  # Reutiliza el mismo modelo base
