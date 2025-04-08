from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from schemas.property_schema import PropertyCreate, PropertyUpdate  # Corregir importaciones
import models

class PropertyController:
    @staticmethod
    def get_property(db: Session, property_id: int):
        return db.query(models.Property).filter(models.Property.id == property_id).first()
    
    @staticmethod
    def get_properties(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Property).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_property(db: Session, property: PropertyCreate):  # Usar PropertyCreate
        db_property = models.Property(
            numberFile=property.numberFile,
            city=property.city,
            address=property.address,
            province=property.province,
            postal_code=property.postal_code,
            type=property.type,
            description=property.description,
            price=property.price,
            owner_id=property.owner_id,
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )
        db.add(db_property)
        db.commit()
        db.refresh(db_property)
        return db_property

    @staticmethod
    def update_property(db: Session, property_id: int, property: PropertyUpdate):  # Usar PropertyUpdate
        db_property = db.query(models.Property).filter(models.Property.id == property_id).first()
        if not db_property:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
        
        update_data = property.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_property, key, value)
        
        db_property.updated_at = datetime.now(timezone.utc)
        db.commit()
        db.refresh(db_property)
        return db_property

    @staticmethod
    def delete_property(db: Session, property_id: int):
        db_property = db.query(models.Property).filter(models.Property.id == property_id).first()
        if not db_property:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Property not found")
        
        db.delete(db_property)
        db.commit()
        return {"detail": "Property deleted successfully"}