from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class  Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    documento = Column(String(20), unique=True, nullable=True)
    nombre = Column(String(100), nullable=True)
    apellido = Column(String(100), nullable=True)
    telefono = Column(String(15), nullable=True)
    email = Column(String(100), nullable=False)
    direccion = Column(String(255), nullable=False)
    ciudad = Column(String(100), nullable=True)
    pais = Column(String(100), nullable=True)
    codigo_postal = Column(String(10), nullable=True)

    # Relaciones
    tickets_despacho = relationship("TicketDespachoBodega", back_populates="cliente", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Cliente(id={self.id}, documento={self.documento}, nombre={self.nombre}, apellido={self.apellido})>"