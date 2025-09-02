from database import db_connect, close_db_conn, execute_query, commit_changes

def create_student(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono):
    """Crear un nuevo estudiante."""
    try:
        conn = db_connect()
        if conn:
            query = """
            INSERT INTO estudiantes (numero_documento, nombre, apellido, fecha_nacimiento, email, telefono) 
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
            execute_query(conn, query, values)
            commit_changes(conn)
    finally:
        close_db_conn(conn)

def read_students():
    """Buscar todos los estudiantes."""
    try:
        conn = db_connect()
        if conn:
            query = "SELECT * FROM estudiantes"
            res = execute_query(conn, query)
            return res
    finally:
        close_db_conn(conn)

def read_student_by_document(numero_documento):
    """Buscar un estudiante por número de documento."""
    try:
        conn = db_connect()
        if conn:
            query = "SELECT * FROM estudiantes WHERE numero_documento = %s"
            values = (numero_documento,)
            res = execute_query(conn, query, values)
            if res:
                return res[0]
            else:
                return None
    finally:
        close_db_conn(conn)

def update_student_by_document(documento):
    """Actualizar un estudiante existente."""    
    try:
        conn = db_connect()
        if conn:
            student = read_student_by_document(documento)
            if not student:
                raise ValueError("Estudiante no encontrado.")
                
    except ValueError as e:
        print(f"{e}")
    
    except Exception as e:
        print(f"Error inesperado: {e}")
        
    else:
        nombre = input("Ingrese el nuevo nombre (presione ENTER para no modificar): ") or student['nombre']
        apellido = input("Ingrese el nuevo apellido (presione ENTER para no modificar): ") or student['apellido']
        fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento (YYYY-MM-DD) (presione ENTER para no modificar): ") or student['fecha_nacimiento']
        email = input("Ingrese el nuevo email (presione ENTER para no modificar): ") or student['email']
        telefono = input("Ingrese el nuevo teléfono (presione ENTER para no modificar): ") or student['telefono']
        
        query = "UPDATE estudiantes SET nombre = %s, apellido = %s, fecha_nacimiento = %s, email = %s, telefono = %s WHERE numero_documento = %s"
        values = (nombre, apellido, fecha_nacimiento, email, telefono, documento)
        execute_query(conn, query, values)
        commit_changes(conn)                
    finally:
        close_db_conn(conn)

def delete_student(numero_documento):
    """Eliminar un estudiante por número de documento."""
    try:
        conn = db_connect()
        if conn:
            query = "DELETE FROM estudiantes WHERE numero_documento = %s"
            values = (numero_documento,)
            execute_query(conn, query, values)
            commit_changes(conn)
    finally:
        close_db_conn(conn)