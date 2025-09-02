from database import db_connect, close_db_conn, execute_query, commit_changes


def create_registration(id_estudiante, id_curso, fecha_inscripcion):
    """Crear un nuevo estudiante."""
    try:
        conn = db_connect()
        if conn:
            query = """
            INSERT INTO inscripciones (id_estudiante, id_curso, fecha_inscripcion) 
            VALUES (%s, %s, %s)
            """
            values = (id_estudiante, id_curso, fecha_inscripcion)
            execute_query(conn, query, values)
            commit_changes(conn)
    finally:
        close_db_conn(conn)

def read_registrations():
    """Consulta todas las inscripciones."""
    try:
        conn = db_connect()
        if conn:
            query = """
            SELECT i.id_inscripcion,
                    e.numero_documento, 
                    e.nombre,
                    e.apellido, 
                    c.id_curso, 
                    c.nombre_curso, 
                    i.fecha_inscripcion 
            FROM inscripciones i 
                INNER JOIN estudiantes e ON i.id_estudiante = e.id_estudiante 
                INNER JOIN cursos c ON i.id_curso = c.id_curso;
                """
            res = execute_query(conn, query)
            return res
    finally:
        close_db_conn(conn)
        
def read_inscription_by_id(id_inscripcion):
    """Buscar una inscripción por ID."""
    try:
        conn = db_connect()
        if conn:
            query = "SELECT * FROM inscripciones WHERE id_inscripcion = %s"
            values = (id_inscripcion,)
            res = execute_query(conn, query, values)
            if res:
                return res[0]
            else:
                return None
    finally:
        close_db_conn(conn)
        
def update_registration_by_id(id):
    """Actualizar un inscripción existente."""    
    try:
        conn = db_connect()
        if conn:
            registration = read_inscription_by_id(id)
            if not registration:
                raise ValueError("Inscripcipon no encontrada.")
                
    except ValueError as e:
        print(f"{e}")
    
    except Exception as e:
        print(f"Error inesperado: {e}")
        
    else:
        id_student = input("Ingrese el nuevo ID de estudiante (presione ENTER para no modificar): ") or registration['id_estudiante']
        id_course = input("Ingrese el nuevo ID de curso (presione ENTER para no modificar): ") or registration['id_curso']
        registration_date = input("Ingrese la nueva fecha de inscripción (YYYY-MM-DD) (presione ENTER para no modificar): ") or registration['fecha_inscripcion']
        
        query = "UPDATE inscripciones SET id_estudiante = %s, id_curso = %s, fecha_inscripcion = %s WHERE id_inscripcion = %s"
        values = (id_student, id_course, registration_date, id)
        execute_query(conn, query, values)
        commit_changes(conn)                
    finally:
        close_db_conn(conn)
        
def delete_registration(id_inscripcion):
    """Eliminar una inscripción por ID."""
    try:
        conn = db_connect()
        if conn:
            query = "DELETE FROM inscripciones WHERE id_inscripcion = %s"
            values = (id_inscripcion,)
            execute_query(conn, query, values)
            commit_changes(conn)
    finally:
        close_db_conn(conn)