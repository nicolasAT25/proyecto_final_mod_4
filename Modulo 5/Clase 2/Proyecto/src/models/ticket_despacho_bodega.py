from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base
import enum

class EstadoTicketDespacho(enum.Enum):
    PENDIENTE = "Pendiente"
    EN_PROCESO = "En Proceso"
    DESPACHADO = "Despachado"
    COMPLETADO = "Completado"
    CANCELADO = "Cancelado"

class TicketDespachoBodega(Base):
    __tablename__ = "ticket_despacho_bodega"
    
    id = Column(Integer, primary_key=True)
    medicamento_id = Column(Integer, ForeignKey("medicamentos.id"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    fecha_solicitud = Column(DateTime, server_default=func.now(), nullable=False)
    estado = Column(Enum(EstadoTicketDespacho), default=EstadoTicketDespacho.PENDIENTE, nullable=False)

    # Relaciones
    medicamento = relationship("Medicamento", back_populates="tickets_despacho")
    cliente = relationship("Cliente", back_populates="tickets_despacho")

    def __repr__(self):
        return f"<TicketDespachoBodega(id={self.id}, medicamento_id={self.medicamento_id}, cantidad={self.cantidad}, cliente_id={self.cliente_id}, fecha_solicitud={self.fecha_solicitud}, estado={self.estado})>"