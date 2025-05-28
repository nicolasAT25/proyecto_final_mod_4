from sqlalchemy.orm import Session
from database.crud import (
    get_all,
    get_by_id,
    get_by_attribute,
    create_item,
    update_item,
    delete_item,
)
from models import Inventario, Medicamento, Ubicacion
from models.ubicacion import TipoUbicacion

# --- Gestion de Medicamentos ---

def add_medicamento(db: Session, nombre: str, descripcion: str = None, codigo_barras: str = None):
    """
    Agrega un nuevo medicamento a la base de datos.
    """
    medicamento_data = {
        "nombre": nombre,
        "descripcion": descripcion,
        "codigo_barras": codigo_barras
    }
    return create_item(db, Medicamento, medicamento_data)

def get_medicamento_by_name(db: Session, nombre: str):
    """
    Obtiene un medicamento por su nombre.
    """
    return get_by_attribute(db, Medicamento, "nombre", nombre)

def get_medicamento_by_id(db: Session, medicamento_id: int):
    """
    Obtiene un medicamento por su ID.
    """
    return get_by_id(db, Medicamento, medicamento_id)

def get_all_medicamentos(db: Session):
    """
    Obtiene todos los medicamentos de la base de datos.
    """
    return get_all(db, Medicamento)

def update_medicamento(db: Session, medicamento_id: int, new_data: dict):
    """
    Actualiza un medicamento existente en la base de datos.
    """
    medicamento = get_medicamento_by_id(db, medicamento_id)
    if medicamento:
        return update_item(db, medicamento, new_data)
    return None

def delete_medicamento(db: Session, medicamento_id: int):
    """
    Elimina un medicamento de la base de datos.
    """
    medicamento = get_medicamento_by_id(db, medicamento_id)
    if medicamento:
        return delete_item(db, medicamento)
    return False

# --- Gestion de Ubicaciones ---
def add_ubicacion(db: Session,  nombre: str, tipo: TipoUbicacion):
    """
    Agrega una nueva ubicacion a la base de datos.
    """
    ubicacion_data = {
        "nombre": nombre,
        "tipo": tipo
    }
    return create_item(db, Ubicacion, ubicacion_data)

def get_ubicacion_by_name(db: Session, nombre: str):
    """
    Obtiene una ubicacion por su nombre.
    """
    return get_by_attribute(db, Ubicacion, "nombre", nombre)

def get_ubicacion_by_id(db: Session, ubicacion_id: int):
    """
    Obtiene una ubicacion por su ID.
    """
    return get_by_id(db, Ubicacion, ubicacion_id)

def get_all_ubicaciones(db: Session):
    """
    Obtiene todas las ubicaciones de la base de datos.
    """
    return get_all(db, Ubicacion)

def update_ubicacion(db: Session, ubicacion_id: int, new_data: dict):
    """
    Actualiza una ubicacion existente en la base de datos.
    """
    ubicacion = get_ubicacion_by_id(db, ubicacion_id)
    if ubicacion:
        return update_item(db, Ubicacion, ubicacion_id, new_data)
    return None

def delete_ubicacion(db: Session, ubicacion_id: int):
    """
    Elimina una ubicacion de la base de datos.
    """
    ubicacion = get_ubicacion_by_id(db, ubicacion_id)
    if ubicacion:
        return delete_item(db, ubicacion)
    return False

# --- Gestion de Inventarios ---

def add_inventario(db: Session, medicamento_id: int, ubicacion_id: int, cantidad: int):
    """
    Agrega un nuevo inventario a la base de datos.
    """
    inventario_data = {
        "medicamento_id": medicamento_id,
        "ubicacion_id": ubicacion_id,
        "cantidad": cantidad
    }
    return create_item(db, Inventario, inventario_data) 

def get_stock_by_medicamento_and_ubicacion(db: Session, medicamento_id: int, ubicacion_id: int):
    """
    Obtiene el stock de un medicamento en una ubicacion especifica.
    """
    return db.query(Inventario).filter(
        Inventario.medicamento_id == medicamento_id,
        Inventario.ubicacion_id == ubicacion_id
    ).first()

def get_inventario_by_ubicacion(db: Session, ubicacion_id: int):
    """
    Obtiene todos los inventarios de una ubicacion especifica.
    """
    return db.query(Inventario).filter(Inventario.ubicacion_id == ubicacion_id).all()

def get_inventario_by_medicamento(db: Session, medicamento_id: int):
    """
    Obtiene todos los inventarios de un medicamento especifico.
    """
    return db.query(Inventario).filter(Inventario.medicamento_id == medicamento_id).all()

def get_inventario_all(db: Session):
    """
    Obtiene todos los inventarios de la base de datos.
    """
    return get_all(db, Inventario)

def update_stock(db: Session, inventario_id: int, ubicacion_id: int, medicamento_id: int, cantidad_a_sumar: int):
    """
    Actualiza un inventario existente en la base de datos.
    """
    inventario_item = get_stock_by_medicamento_and_ubicacion(db, medicamento_id, ubicacion_id)
    if inventario_item:
        new_quantity = inventario_item.cantidad + cantidad_a_sumar
        if new_quantity < 0:
            print("Error: la cantidad no puede ser negativa.")
            return None
        return update_item(db, Inventario, inventario_id, {"cantidad": new_quantity})
    else:
        if cantidad_a_sumar < 0:
            print("Error: no se puede agregar stock a un medicamento no existente.")
            return None
        inventario_data = {
            "medicamento_id": medicamento_id,
            "ubicacion_id": ubicacion_id,
            "cantidad": cantidad_a_sumar
        }
        return create_item(db, Inventario, inventario_data)

def delete_inventario(db: Session, inventario_id: int):
    """
    Elimina un inventario de la base de datos.
    """
    inventario = get_by_id(db, Inventario, inventario_id)
    if inventario:
        return delete_item(db, inventario)
    return False
