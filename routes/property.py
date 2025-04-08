from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from helpers.dependencies import get_db
from schemas.property_schema import (
    PropertyCreate,
    PropertyUpdate,
    PropertyResponse,
    PropertyListResponse,
)
from controllers import PropertyController

PropertyRouter = APIRouter(prefix="/api/property", tags=["property"])
@PropertyRouter.post("/", response_model=PropertyResponse)
def create_property(property: PropertyCreate, db: Session = Depends(get_db)):
    return PropertyController.create_property(property, db)
@PropertyRouter.get("/{property_id}", response_model=PropertyResponse)
def get_property(property_id: int, db: Session = Depends(get_db)):
    return PropertyController.get_property(property_id, db)
@PropertyRouter.get("/", response_model=PropertyListResponse)
def get_properties(db: Session = Depends(get_db)):
    return PropertyController.get_properties(db)
@PropertyRouter.put("/{property_id}", response_model=PropertyResponse)
def update_property(property_id: int, property: PropertyUpdate, db: Session = Depends(get_db)):
    return PropertyController.update_property(property_id, property, db)
@PropertyRouter.delete("/{property_id}", response_model=PropertyResponse)
def delete_property(property_id: int, db: Session = Depends(get_db)):
    return PropertyController.delete_property(property_id, db)