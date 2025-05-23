from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, NoResultFound

# -- Funciones de Lectura(Read) --
def get_all(db: Session, model, skip: int = 0, limit: int = 100):
    """
    Obtener todos los registros de un modelo.
    :param db: Sesión de la base de datos.
    :param model: Modelo a consultar.
    :param skip: Número de registros a omitir.
    :param limit: Número máximo de registros a devolver.
    :return: Lista de registros del modelo.
    """
    return db.query(model).offset(skip).limit(limit).all()

def get_by_id(db: Session, model, record_id: int):
    """
    Obtener un registro por su ID.
    :param db: Sesión de la base de datos.
    :param model: Modelo a consultar.
    :param record_id: ID del registro a buscar.
    :return: Registro del modelo o None si no se encuentra.
    """
    return db.query(model).filter(model.id == record_id).first()

def get_by_attribute(db: Session, model, attribute: str, value):
    """
    Obtener un registro por un atributo específico.
    :param db: Sesión de la base de datos.
    :param model: Modelo a consultar.
    :param attribute: Atributo a buscar.
    :param value: Valor del atributo a buscar.
    :return: Registro del modelo o None si no se encuentra.
    """
    return db.query(model).filter(getattr(model, attribute) == value).first()

# --- Funciones de Escritura(Create) ---
def create_item(db: Session, model, item_data: dict):
    """
    Crear un nuevo registro en la base de datos.
    :param db: Sesión de la base de datos.
    :param model: Modelo a utilizar.
    :param item_data: Datos del nuevo registro.
    :return: Registro creado o None si ocurre un error.
    """
    try:
        db_item = model(**item_data)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    except IntegrityError as e:
        db.rollback()
        print(f"Error al crear {model.__name__}: {e}: Ya existe un registro con esos datos.")
        return None
    except Exception as e:
        db.rollback()
        print(f"Error al crear {model.__name__}: {e}")
        return None
    
# --- Funciones de Actualización(Update) ---
def update_item(db: Session, db_item, update_data: dict):
    """
    Actualizar un registro existente en la base de datos.
    :param db: Sesión de la base de datos.
    :param db_item: Registro a actualizar.
    :param update_data: Datos a actualizar.
    :return: Registro actualizado o None si ocurre un error.
    """
    try:
        for key, value in update_data.items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
        return db_item
    except IntegrityError as e:
        db.rollback()
        print(f"Error al actualizar {db_item.__class__.__name__}: {e}")
        return None
    except Exception as e:
        db.rollback()
        print(f"Error al actualizar {db_item.__class__.__name__}: {e}")
        return None

# --- Funciones de Eliminación(Delete) ---
def delete_item(db: Session, db_item):
    """
    Eliminar un registro de la base de datos.
    :param db: Sesión de la base de datos.
    :param db_item: Registro a eliminar.
    :return: True si se elimina correctamente, False en caso contrario.
    """
    try:
        db.delete(db_item)
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()
        print(f"Error al eliminar {db_item.__class__.__name__}: {e}")
        return False
    except Exception as e:
        db.rollback()
        print(f"Error al eliminar {db_item.__class__.__name__}: {e}")
        return False