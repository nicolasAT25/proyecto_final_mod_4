import uuid
from sqlalchemy import create_engine, Column, String, Numeric, Text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.dialects.postgresql import UUID

DATABASE_URI = "postgresql://postgres:Admin@localhost:5432/Academia"

engine = create_engine(DATABASE_URI)
Base = declarative_base()

class Empleado(Base):
    __tablename__ = "empleados"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(100), nullable=False)
    puesto = Column(String(100), nullable=False)
    salario = Column(Numeric, nullable=False)

    def __repr__(self):
        return f"Empleado(id={self.id}, nombre={self.nombre}, puesto={self.puesto}, salario={self.salario})"
    
def crear_empleado(nombre, puesto, salario):
    empleado = Empleado(nombre=nombre, puesto=puesto, salario=salario)
    session.add(empleado)
    session.commit()
    print(f"Empleado '{empleado.nombre}' creado con éxito.")


#Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
#crear_empleado("Juan", "Programador", 5000)
crear_empleado("Maria", "Diseñadora", 6000)