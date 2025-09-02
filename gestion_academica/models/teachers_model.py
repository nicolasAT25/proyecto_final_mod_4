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

def update_teacher(numero_documento):
    """Actualizar un docente existente."""
    try:
        conn = db_connect()
        if conn:
            teacher = read_teacher_by_document(numero_documento)
            if not teacher:
                raise ValueError("Docente no encontrado.")
            
    except ValueError as e:
        print(f"{e}")
        
    except Exception as e:
        print(f"Error inesperado: {e}")
        
    else:
        nombre = input("Ingrese el nuevo nombre (presione ENTER para no modificar): ") or teacher['nombre']
        apellido = input("Ingrese el nuevo apellido (presione ENTER para no modificar): ") or teacher['apellido']
        email = input("Ingrese el nuevo email (presione ENTER para no modificar): ") or teacher['email']
        telefono = input("Ingrese el nuevo teléfono (presione ENTER para no modificar): ") or teacher['telefono']
        especialidad = input("Ingrese la nueva especialidad (presione ENTER para no modificar): ") or teacher['especialidad']
        
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