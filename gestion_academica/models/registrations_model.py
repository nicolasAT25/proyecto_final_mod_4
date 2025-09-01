from database import db_connect, close_db_conn, execute_query, commit_changes


# Consultar todos los inscripciones
def read_inscriptions():
    """Consulta todos los cursos."""
    try:
        conn = db_connect()
        if conn:
            query = """
            SELECT i.id_inscripcion,
                    e.numero_documento, 
                    e.nombre, e.apellido, 
                    c.id_curso, 
                    c.nombre_curso, 
                    i.fecha_inscripcion 
            FROM inscripciones i 
                JOIN estudiantes e ON i.id_estudiante = e.id_estudiante 
                JOIN cursos c ON i.id_curso = c.id_curso;
                """
            res = execute_query(conn, query)
            return res
    finally:
        close_db_conn(conn)