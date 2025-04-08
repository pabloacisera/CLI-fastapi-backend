from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from schemas.owner_schema import OwnerCreate, OwnerUpdate  # Corregir importaciones
import models

class OwnerController:
    @staticmethod
    def get_owner(db: Session, owner_id: int):
        return db.query(models.Owner).filter(models.Owner.id == owner_id).first()

    @staticmethod
    def get_owner_by_dni(db: Session, dni: str):
        return db.query(models.Owner).filter(models.Owner.dni == dni).first()
    
    @staticmethod
    def get_owners(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Owner).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_owner(db: Session, owner: OwnerCreate):
        db_owner = models.Owner(
            name=owner.name,
            address=owner.address,
            city=owner.city,
            dni=owner.dni,
            cuit=owner.cuit,
            phone=owner.phone,
            email=owner.email,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        db.add(db_owner)
        db.commit()
        db.refresh(db_owner)
        return db_owner

    @staticmethod
    def update_owner(db: Session, owner_id: int, owner: OwnerUpdate):
        db_owner = db.query(models.Owner).filter(models.Owner.id == owner_id).first()
        if not db_owner:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Owner not found")
        
        update_data = owner.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_owner, key, value)
        
        db_owner.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(db_owner)
        return db_owner

    @staticmethod
    def delete_owner(db: Session, owner_id: int):
        db_owner = db.query(models.Owner).filter(models.Owner.id == owner_id).first()
        if not db_owner:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Owner not found")
        
        db.delete(db_owner)
        db.commit()
        return {"detail": "Owner deleted successfully"}
            