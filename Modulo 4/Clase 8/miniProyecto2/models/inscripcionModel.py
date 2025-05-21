from database import conectar_db, cerrar_db, ejecutar_consulta, confirmar_cambios


# Consultar todos los inscripciones
def consultarInscripciones():
    """Consulta todos los cursos."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "SELECT i.id_inscripcion, e.numero_documento, e.nombre, e.apellido, c.id_curso, c.nombre_curso, i.fecha_inscripcion FROM inscripciones i JOIN estudiantes e ON i.id_estudiante = e.id_estudiante JOIN cursos c ON i.id_curso = c.id_curso;"
            resultados = ejecutar_consulta(conexion, consulta)
            return resultados
    finally:
        cerrar_db(conexion)