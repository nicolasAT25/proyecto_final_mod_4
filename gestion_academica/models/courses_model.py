from database import db_connect, close_db_conn, execute_query

def read_courses():
    """Consulta todos los cursos."""
    try:
        conn = db_connect()
        if conn:
            query = """SELECT c.id_curso, 
                            c.nombre_curso, 
                            c.descripcion, 
                            c.creditos, 
                            d.nombre AS nombre_docenente, 
                            d.apellido as apellido_docente 
                        FROM cursos c JOIN docentes d ON c.id_docente = d.id_docente;"""
            resultados = execute_query(conn, query)
            return resultados
    finally:
        close_db_conn(conn)

# Consulta un curso por el id del docente
def read_course_by_teacher_id(id_docente):
    """Consulta un curso por el id del docente."""
    try:
        conn = db_connect()
        if conn:
            query = """
            SELECT c.nombre_curso, 
                    c.descripcion, 
                    c.creditos, 
                    d.nombre AS nombre_docenente, 
                    d.apellido as apellido_docente 
            FROM cursos c 
                JOIN docentes d ON c.id_docente = d.id_docente 
            WHERE d.id_docente = %s;
            """
            res = execute_query(conn, query, (id_docente,))
            return res
    finally:
        close_db_conn(conn)

# Consulta un curso por el id del curso
def read_course_by_id(id_curso):
    """Consulta un curso por el id del docente."""
    try:
        conn = db_connect()
        if conn:
            query = """
            SELECT c.nombre_curso, 
                    c.descripcion, 
                    c.creditos, 
                    d.nombre AS nombre_docenente, 
                    d.apellido as apellido_docente 
            FROM cursos c 
                JOIN docentes d ON c.id_docente = d.id_docente 
            WHERE d.id_curso = %s;
            """
            res = execute_query(conn, query, (id_curso,))
            return res
    finally:
        close_db_conn(conn)