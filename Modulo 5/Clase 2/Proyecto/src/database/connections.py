from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

#Importar Base
from src.models.base import Base

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'data', 'sigid_med.db')}"

# Crear el motor de la base de datos
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # Solo necesario para SQLite
    echo=True,  # Para ver las consultas SQL generadas
)

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear todas las tablas en la base de datos
def create_db_tables():
    Base.metadata.create_all(bind=engine)
    print("Base de datos y tablas creadas con éxito.")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()