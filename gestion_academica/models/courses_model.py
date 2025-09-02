from database import db_connect, close_db_conn, execute_query, commit_changes

def create_course(nombre_curso, descripcion, creditos, id_docente):
    """Crear un nuevo estudiante."""
    try:
        conn = db_connect()
        if conn:
            query = """
            INSERT INTO cursos (nombre_curso, descripcion, creditos, id_docente) 
            VALUES (%s, %s, %s, %s)
            """
            values = (nombre_curso, descripcion, creditos, id_docente)
            execute_query(conn, query, values)
            commit_changes(conn)
    finally:
        close_db_conn(conn)

def read_courses():
    """Consulta todos los cursos."""
    try:
        conn = db_connect()
        if conn:
            query = """
            SELECT c.id_curso, 
                c.nombre_curso, 
                c.descripcion, 
                c.creditos, 
                d.nombre AS nombre_docente, 
                d.apellido as apellido_docente 
            FROM cursos c 
                LEFT JOIN docentes d ON c.id_docente = d.id_docente;"""
            res = execute_query(conn, query)
            return res
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
                    d.nombre AS nombre_docente, 
                    d.apellido as apellido_docente 
            FROM cursos c 
                LEFT JOIN docentes d ON c.id_docente = d.id_docente 
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
                    d.nombre AS nombre_docente, 
                    d.apellido as apellido_docente 
            FROM cursos c 
                LEFT JOIN docentes d ON c.id_docente = d.id_docente
            WHERE c.id_curso = %s;
            """
            res = execute_query(conn, query, (id_curso,))
            return res[0]
    finally:
        close_db_conn(conn)
        
def update_course_by_id(id):
    """Actualizar un curso existente."""    
    try:
        conn = db_connect()
        if conn:
            query_course = """
            SELECT * FROM cursos WHERE id_curso = %s
            """
            course = execute_query(conn, query_course, (id,))[0]
            if not course:
                raise ValueError("Curso no encontrado.")
            print(course)
                
    except ValueError as e:
        print(f"{e}")
    
    except Exception as e:
        print(f"Error inesperado: {e}")
        
    else:
        nombre_curso = input("Ingrese el nuevo nombre (presione ENTER para no modificar): ") or course['nombre_curso']
        descripcion = input("Ingrese la nueva descripción (presione ENTER para no modificar): ") or course['descripcion']
        creditos = input("Ingrese los nuevos créditos (presione ENTER para no modificar): ") or course['creditos']
        id_docente = input("Ingrese el nuevo ID de docente (presione ENTER para no modificar): ") or course['id_docente']
        
        query = "UPDATE cursos SET nombre_curso = %s, descripcion = %s, creditos = %s, id_docente = %s WHERE id_curso = %s"
        values = (nombre_curso, descripcion, creditos, id_docente, id)
        execute_query(conn, query, values)
        commit_changes(conn)                
    finally:
        close_db_conn(conn)
        
def delete_course(id_curso):
    """Eliminar un curso por número ID."""
    try:
        conn = db_connect()
        if conn:
            query = "DELETE FROM cursos WHERE id_curso = %s"
            values = (id_curso,)
            execute_query(conn, query, values)
            commit_changes(conn)
    finally:
        close_db_conn(conn)