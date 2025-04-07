from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
logging.getLogger("sqlalchemy.dialects.mysql").setLevel(logging.INFO)
logging.getLogger("sqlalchemy.pool").setLevel(logging.INFO)

# Database URL
password_escaped = quote_plus(settings.MYSQL_PASSWORD)
DATABASE_URL = f"mysql+pymysql://{settings.MYSQL_USER}:{password_escaped}@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.MYSQL_DATABASE}"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, pool_recycle=3600, echo=True)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Create a session instance
Base = declarative_base()

def check_connection():
    try:
        with engine.connect():
            print("Database connection successful")
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise()