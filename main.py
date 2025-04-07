from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from routes.auth import AuthRouter
import models

#crear tablas(development)
models.Base.metadata.create_all(bind=engine)

# Crear la aplicación FastAPI
app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto a la lista de dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(AuthRouter)
