import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.')/'.env'

load_dotenv(dotenv_path=env_path)

class Settings:

    MYSQL_USER=os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD=os.getenv("MYSQL_PASSWORD", " ")
    MYSQL_HOST=os.getenv("MYSQL_HOST", "localhost")
    MYSQL_PORT=os.getenv("MYSQL_PORT", "3306")
    MYSQL_DATABASE=os.getenv("MYSQL_DB", "facture_app")
    SECRET_KEY=os.getenv("SECRET_KEY")
    ALGORITHM=os.getenv("ALGORITHM", "HS256")
    EXPIRES_IN=os.getenv("EXPIRES_IN", "30")

settings = Settings()