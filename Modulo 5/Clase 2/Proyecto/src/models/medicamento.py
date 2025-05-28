from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base

class Medicamento(Base):
    __tablename__ = "medicamentos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100),nullable=False)
    descripcion = Column(String(255),nullable=False)
    codigo_barras = Column(String(100), unique=True , nullable=False)

    #Relaciones
    inventarios = relationship("Inventario", back_populates="medicamento", cascade="all, delete-orphan")
    tickets_despacho = relationship("TicketDespachoBodega", back_populates="medicamento", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Medicamento(id={self.id}, nombre={self.nombre}, codigo_barras={self.codigo_barras})>"