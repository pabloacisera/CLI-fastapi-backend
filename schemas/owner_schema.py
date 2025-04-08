from datetime import datetime
from pydantic import BaseModel, EmailStr, Field

class OwnerBase(BaseModel):
    name: str = Field(..., max_length=100)
    address: str = Field(..., max_length=200)
    city: str = Field(..., max_length=100)
    dni: str = Field(..., max_length=50)
    cuit: str = Field(..., max_length=50)
    phone: str = Field(..., max_length=50)
    email: EmailStr = Field(..., max_length=100)

class OwnerCreate(OwnerBase):
    pass

class OwnerUpdate(BaseModel):
    name: str = Field(None, max_length=100)
    address: str = Field(None, max_length=200)
    city: str = Field(None, max_length=100)
    dni: str = Field(None, max_length=50)
    cuit: str = Field(None, max_length=50)
    phone: str = Field(None, max_length=50)
    email: EmailStr = Field(None, max_length=100)

class Owner(OwnerBase):
    id: int
    created_at: datetime
    updated_at: datetime

class OwnerResponse(BaseModel):
    success: bool = True
    message: str = "Operation successful"
    data: Owner

class OwnerListResponse(BaseModel):
    success: bool = True
    count: int
    data: list[Owner]
