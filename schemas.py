from enum import Enum
from pydantic import BaseModel, EmailStr

class Role(str, Enum):
    USER="USER"
    ADMIN="ADMIN"
    GUEST="GUEST"

class UserCreate(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str
    role: Role = Role.USER

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type:str

class UserResponseRegister(BaseModel):
    id:int
    name:str
    username: str
    email: EmailStr
    role: Role

    class Config:
        orm_mode = True

class UserResponseLogin(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    role: Role
    token: Token

    class Config:
        orm_mode = True
