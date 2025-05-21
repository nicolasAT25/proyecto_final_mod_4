from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Configuración de la base de datos
DATABASE_URL = "mysql+pymysql://root:admin@localhost:3306/academiaPython"
engine = create_engine(DATABASE_URL, echo=True)

# Declarative base
Base = declarative_base()

# Definición de la tabla
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    edad = Column(Integer)

# Crear la tabla en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crear un nuevo usuario
nuevo_usuario = Usuario(nombre="Juan", apellido="Pérez", edad=30)
session.add(nuevo_usuario)  
session.commit()  # Guardar los cambios en la base de datos

