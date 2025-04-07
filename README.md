markdown
Copy
# 🔐 Auth API con FastAPI y MySQL

API de autenticación con registro de usuarios, login y generación de tokens JWT.

## 🚀 Empezar

### 📋 Prerequisitos
- Python 3.7+
- MySQL 5.7+
- pip

### ⚙️ Configuración
1. Clonar repositorio
2. Crear entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows
Instalar dependencias:

bash
Copy
pip install fastapi uvicorn python-dotenv pymysql sqlalchemy passlib python-jose[cryptography]
Configurar .env:

env
Copy
MYSQL_USER=root
MYSQL_PASSWORD=tu_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=auth_db
SECRET_KEY=tu_clave_secreta
ALGORITHM=HS256
EXPIRES_IN=30
Ejecutar:

bash
Copy
uvicorn main:app --reload
🏗️ Estructura del Proyecto
Copy
.
├── main.py                # App principal
├── config.py              # Configuración
├── database.py            # Conexión DB
├── models.py              # Modelos DB
├── schemas.py             # Schemas Pydantic
├── routes/                # Endpoints
│   └── auth.py            # Rutas auth
└── controllers/           # Lógica
    └── auth_controller.py # Controlador auth
📡 Endpoints
🆕 Registrar usuario
POST /api/auth/register

json
Copy
{
  "name": "Nombre",
  "username": "usuario123",
  "email": "email@ejemplo.com",
  "password": "contraseñaSegura",
  "role": "USER"
}
🔑 Login
POST /api/auth/login

json
Copy
{
  "email": "email@ejemplo.com",
  "password": "contraseñaSegura"
}
🧑‍💻 Modelo User
python
Copy
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    username = Column(String(50))
    email = Column(String(100), unique=True)
    password = Column(String(100))
    is_active = Column(Boolean, default=False)
    role = Column(String(50), default='USER')
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())
🛡️ Seguridad
Hashing de contraseñas con Passlib

Tokens JWT firmados

Validación con Pydantic

CORS configurado

📅 Roadmap
Verificación por email

Recuperación de contraseña

Roles y permisos

Documentación Swagger

🤝 Contribuir
Haz fork al proyecto

Crea tu feature branch

Haz commit de tus cambios

Push a la rama

Abre Pull Request

📄 Licencia MIT

Copy

Este archivo contiene:
1. Instrucciones claras de instalación
2. Estructura del proyecto
3. Documentación de endpoints
4. Modelo de datos
5. Información de seguridad
6. Roadmap
7. Guía de contribución

Puedes copiar TODO este contenido directamente a tu archivo README.md