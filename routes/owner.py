from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from helpers.dependencies import get_db
from schemas.owner_schema import (
    OwnerCreate,
    OwnerUpdate,
    OwnerResponse,
)
from controllers import OwnerController

OwnerRouter = APIRouter(prefix="/api/owner", tags=["owner"])

@OwnerRouter.post("/", response_model=OwnerResponse)
def create_owner(owner: OwnerCreate, db: Session = Depends(get_db)):
    return OwnerController.create_owner(owner, db)

@OwnerRouter.get("/{owner_id}", response_model=OwnerResponse)
def get_owner(owner_id: int, db: Session = Depends(get_db)):
    return OwnerController.get_owner(owner_id, db)

@OwnerRouter.put("/{owner_id}", response_model=OwnerResponse)
def update_owner(owner_id: int, owner: OwnerUpdate, db: Session = Depends(get_db)):
    return OwnerController.update_owner(owner_id, owner, db)

@OwnerRouter.delete("/{owner_id}", response_model=OwnerResponse)
def delete_owner(owner_id: int, db: Session = Depends(get_db)):
    return OwnerController.delete_owner(owner_id, db)

@OwnerRouter.get("/", response_model=list[OwnerResponse])
def get_owners(db: Session = Depends(get_db)):
    return OwnerController.get_owners(db)
