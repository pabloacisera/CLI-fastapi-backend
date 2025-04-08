from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserLogin, RegisterResponse, LoginResponse
from auth import get_password_hash, verify_password, create_access_token

def register(user: UserCreate, db: Session) -> RegisterResponse:
    """
    Registra un nuevo usuario y devuelve la respuesta estructurada
    """
    print("Datos obtenidos en el backend: ", user)

    # Verificar si el usuario ya existe
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)

    # Crear nuevo usuario
    new_user = User(
        name=user.name,
        username=user.username,
        email=user.email,
        password=hashed_password,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Convertimos el objeto SQLAlchemy a un diccionario compatible con UserBase
    user_data = {
        "id": new_user.id,
        "name": new_user.name,
        "username": new_user.username,
        "email": new_user.email,
        "role": new_user.role
    }

    
    return RegisterResponse(
        message="User registered successfully",
        user=user_data  # SQLAlchemy automáticamente mapea al UserBase
    )

def login(user: UserLogin, db: Session) -> LoginResponse:
    """
    Autentica un usuario y devuelve la respuesta con token
    """
    print("Datos obtenidos en el backend: ", user)
    
    # Verificar si el usuario existe
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Verificar la contraseña
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    # Generar token JWT
    access_token = create_access_token(data={"sub": db_user.email})

    user_data = {
        "id": db_user.id,
        "name": db_user.name,
        "username": db_user.username,
        "email": db_user.email,
        "role": db_user.role
    }

    return LoginResponse(
        access_token=access_token,
        token_type="bearer",
        user=user_data  # SQLAlchemy automáticamente mapea al UserBase
    )