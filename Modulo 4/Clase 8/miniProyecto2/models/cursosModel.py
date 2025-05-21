from database import conectar_db, cerrar_db, ejecutar_consulta, confirmar_cambios

def consultarCursos():
    """Consulta todos los cursos."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "SELECT c.id_curso, c.nombre_curso, c.descripcion, c.creditos, d.nombre AS nombre_docenente, d.apellido as apellido_docente FROM cursos c JOIN docentes d ON c.id_docente = d.id_docente;"
            resultados = ejecutar_consulta(conexion, consulta)
            return resultados
    finally:
        cerrar_db(conexion)

# Consulta un curso por el id del docente
def consultarCursoPorDocente(id_docente):
    """Consulta un curso por el id del docente."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "SELECT c.nombre_curso, c.descripcion, c.creditos, d.nombre AS nombre_docenente, d.apellido as apellido_docente FROM cursos c JOIN docentes d ON c.id_docente = d.id_docente WHERE d.numero_documento = %s;"
            resultados = ejecutar_consulta(conexion, consulta, (id_docente,))
            return resultados
    finally:
        cerrar_db(conexion)