from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    username = Column(String(50), unique=False, index=True)
    email = Column(String(100), unique=True, index=True)
    password = Column(String(100))
    is_active = Column(Boolean, default=False)
    role = Column(String(50), default='USER')
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, username={self.username}, email={self.email}, role={self.role}), is_active={self.is_active}, created_at={self.created_at}, updated_at={self.updated_at})"

class Owner(Base):
    __tablename__ = 'owners'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    address = Column(String(200), index=True)
    city = Column(String(100), index=True)
    dni = Column(String(50), index=True)
    cuit = Column(String(50), index=True)
    phone = Column(String(50), index=True)
    email = Column(String(100), index=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    properties = relationship("Property", back_populates="owner")

    def __repr__(self):
        return f"Owner(id={self.id}, name={self.name}, address={self.address}, city={self.city}, dni={self.dni}, cuit={self.cuit}, phone={self.phone}, email={self.email}), created_at={self.created_at}, updated_at={self.updated_at})"

class Property(Base):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True, index=True)
    numberFile = Column(String(100), index=True)
    city = Column(String(100), index=True)
    address = Column(String(200), index=True)
    province = Column(String(50), index=True)
    postal_code = Column(String(50), index=True)
    type = Column(String(50), index=True)
    description = Column(String(200), index=True)
    price = Column(Integer, index=True)
   
    owner_id = Column(Integer, index=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    owner = relationship("Owner", back_populates="properties")

    def __repr__(self):
        return f"Property(id={self.id}, numberFile={self.numberFile}, city={self.city}, address={self.address}, province={self.province}, postal_code={self.postal_code}, type={self.type}, description={self.description}, price={self.price}), owner_id={self.owner_id}, created_at={self.created_at}, updated_at={self.updated_at})"