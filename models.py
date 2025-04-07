from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Integer, String
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