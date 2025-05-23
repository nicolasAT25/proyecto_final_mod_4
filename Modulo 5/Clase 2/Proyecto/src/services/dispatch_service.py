from sqlalchemy.orm import Session
from src.database.crud import (
    get_all,
    get_by_id,
    get_by_attribute,
    create_item,
    update_item,
    delete_item,
)
from src.models import Medicamento, Ubicacion, Cliente, TicketDespachoBodega
from src.models.ubicacion import TipoUbicacion
from src.models.ticket_despacho_bodega import EstadoTicket
from src.services.inventory_service import update_stock, get_stock_by_medicamento_and_ubicacion, get_medicamento_by_id,get_ubicacion_by_id

#-- Gestion de Clientes --
def add_cliente(db: Session, documento: str, nombre: str, apellido: str, telefono : str, email: str, direccion: str = None, ciudad: str = None, pais: str = None, codigo_postal: str = None):
    """
    Agrega un nuevo cliente a la base de datos.
    """
    cliente_data = {
        "documento": documento,
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "ciudad": ciudad,
        "pais": pais,
        "codigo_postal": codigo_postal
    }
    return create_item(db, Cliente, cliente_data)
   
def get_cliente_by_documento(db: Session, documento: str):
    """
    Obtiene un cliente por su documento.
    """
    return get_by_attribute(db, Cliente, "documento", documento)

def get_cliente_by_id(db: Session, cliente_id: int):
    """
    Obtiene un cliente por su ID.
    """
    return get_by_id(db, Cliente, cliente_id)

def get_all_clientes(db: Session):
    """
    Obtiene todos los clientes de la base de datos.
    """
    return get_all(db, Cliente)

def update_cliente(db: Session, cliente_id: int, new_data: dict):
    """
    Actualiza un cliente existente en la base de datos.
    """
    cliente = get_cliente_by_id(db, cliente_id)
    if cliente:
        return update_item(db, Cliente, cliente_id, new_data)
    return None

def delete_cliente(db: Session, cliente_id: int):       
    """
    Elimina un cliente de la base de datos.
    """
    cliente = get_cliente_by_id(db, cliente_id)
    if cliente:
        return delete_item(db, cliente)
    return False

#-- logica de despacho --

def displatch_medicamento_from_local(db: Session, medicamento_id: int, local_id: int, cantidad: int, cliente_data: dict=None):
    """
    Despacha un medicamento desde una ubicación local a un cliente.
    """
    # Obtener el medicamento y la ubicación
    medicamento = get_medicamento_by_id(db, medicamento_id)
    local = get_ubicacion_by_id(db, local_id)
    
    if not medicamento:
        return ValueError("Medicamento no encontrado")
    if not local or local.tipo != TipoUbicacion.LOCAL:
        return ValueError("Ubicación no válida o no es un local")
    if cantidad <= 0:
        return ValueError("La cantidad debe ser mayor a cero")
    
    # Verificar el stock disponible
    stock_local_item = get_stock_by_medicamento_and_ubicacion(db, medicamento_id, local_id)
    stock_disponible = stock_local_item.cantidad if stock_local_item else 0

    if stock_disponible >= cantidad:
        update_inventory = update_stock(db, medicamento_id, local_id, -cantidad)
        if update_inventory:
            return True, f"Medicamento {medicamento.nombre} despachado desde {local.nombre} a cliente {cliente_data['nombre']}"
        else:
            return False, "Error al actualizar el inventario"
    else:
        return False, "Stock insuficiente en el local"