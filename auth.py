from passlib.context import CryptContext
from datetime import datetime, timezone, timedelta
from config import settings  # Asegúrate de que 'config' esté correctamente configurado
from jose import jwt

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    
    # Establecemos la expiración con zona horaria UTC
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.EXPIRES_IN)
    
    # Agregamos la expiración al payload
    to_encode.update({
        "exp": expire
    })
    
    # Retornamos el token codificado
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
