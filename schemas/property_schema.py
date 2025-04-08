from datetime import datetime
from pydantic import BaseModel, Field

class PropertyBase(BaseModel):
    numberFile: str = Field(..., max_length=100, example="EXP-2023-001")
    city: str = Field(..., max_length=100, example="Buenos Aires")
    address: str = Field(..., max_length=200, example="Av. Corrientes 1234")
    province: str = Field(..., max_length=50, example="CABA")
    postal_code: str = Field(..., max_length=50, example="C1043")
    type: str = Field(..., max_length=50, example="Departamento", description="Tipo de propiedad: Casa, Departamento, PH, etc.")
    description: str = Field(..., max_length=200, example="Amplio departamento de 3 ambientes")
    price: int = Field(..., gt=0, example=150000)
    owner_id: int = Field(..., gt=0, example=1)

class PropertyCreate(PropertyBase):
    pass

class PropertyUpdate(BaseModel):
    numberFile: str = Field(None, max_length=100, example="EXP-2023-001")
    city: str = Field(None, max_length=100, example="Buenos Aires")
    address: str = Field(None, max_length=200, example="Av. Corrientes 1234")
    province: str = Field(None, max_length=50, example="CABA")
    postal_code: str = Field(None, max_length=50, example="C1043")
    type: str = Field(None, max_length=50, example="Departamento")
    description: str = Field(None, max_length=200, example="Amplio departamento renovado")
    price: int = Field(None, gt=0, example=180000)
    owner_id: int = Field(None, gt=0, example=1)

class Property(PropertyBase):
    id: int
    created_at: datetime
    updated_at: datetime

class PropertyResponse(BaseModel):
    success: bool
    message: str
    data: Property

class PropertyListResponse(BaseModel):
    success: bool
    count: int
    data: list[Property]
