# Modulo 4/Clase 8/miniProyecto2/models/docentesModel.py

from database import db_connect, close_db_conn, execute_query, commit_changes

def create_teacher(numero_documento, nombre, apellido, email, telefono, especialidad):
    """Crear un nuevo docente."""
    try:
        conn = db_connect()
        if conn:
            query = "INSERT INTO docentes (numero_documento, nombre, apellido, email, telefono, especialidad) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (numero_documento, nombre, apellido, email, telefono, especialidad)
            execute_query(conn, query, values)
            commit_changes(conn)
    finally:
        close_db_conn(conn)

def read_teachers():
    """Buscar todos los docentes."""
    try:
        conn = db_connect()
        if conn:
            query = "SELECT * FROM docentes"
            res = execute_query(conn, query)
            return res
    finally:
        close_db_conn(conn)

def read_teacher_by_document(numero_documento):
    """Buscar un docente por número de documento."""
    try:
        conn = db_connect()
        if conn:
            query = "SELECT * FROM docentes WHERE numero_documento = %s"
            values = (numero_documento,)
            res = execute_query(conn, query, values)
            if res:
                return res[0]
            else:
                return None
    finally:
        close_db_conn(conn)

def update_teacher(numero_documento, nombre, apellido, email, telefono, especialidad):
    """Actualizar un docente existente."""
    try:
        conn = db_connect()
        if conn:
            query = "UPDATE docentes SET nombre = %s, apellido = %s, email = %s, telefono = %s, especialidad = %s WHERE numero_documento = %s"
            values = (nombre, apellido, email, telefono, especialidad, numero_documento)
            execute_query(conn, query, values)
            commit_changes(conn)
    finally:
        close_db_conn(conn)

def delete_teacher(numero_documento):
    """Eliminar un docente por número de documento."""
    try:
        conn = db_connect()
        if conn:
            query = "DELETE FROM docentes WHERE numero_documento = %s"
            values = (numero_documento,)
            execute_query(conn, query, values)
            commit_changes(conn)
    finally:
        close_db_conn(conn)