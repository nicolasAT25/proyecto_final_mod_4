from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint
from .base import Base

class Inventario(Base):
    __tablename__ = "inventarios"

    id = Column(Integer, primary_key=True)
    medicamento_id = Column(Integer, ForeignKey("medicamentos.id"), nullable=False)
    ubicacion_id = Column(Integer, ForeignKey("ubicaciones.id"), nullable=False)
    cantidad = Column(Integer, nullable=False, default=0)

    # relaciones
    medicamento = relationship("Medicamento", back_populates="inventarios")
    ubicacion = relationship("Ubicacion", back_populates="inventarios")

    def __repr__(self):
        return f"<Inventario(id={self.id}, medicamento_id={self.medicamento_id}, ubicacion_id={self.ubicacion_id}, cantidad={self.cantidad})>"
