from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from .base import Base
import enum

class TipoUbicacion(enum.Enum):
    BODEGA = "Bodega"
    LOCAL = "Local"

class Ubicacion(Base):
    __tablename__ = "ubicaciones"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False, unique=True)
    tipo = Column(Enum(TipoUbicacion), nullable=False) # Tipo de ubicación (Bodega o Local)

    # Relaciones
    inventarios = relationship("Inventario", back_populates="ubicacion", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Ubicacion(id={self.id}, nombre={self.nombre}, tipo={self.tipo})>"