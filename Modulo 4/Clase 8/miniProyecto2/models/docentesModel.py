# Modulo 4/Clase 8/miniProyecto2/models/docentesModel.py

from database import conectar_db, cerrar_db, ejecutar_consulta, confirmar_cambios

def crear(numero_documento, nombre, apellido, email, telefono, especialidad):
    """Crear un nuevo docente."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "INSERT INTO docentes (numero_documento, nombre, apellido, email, telefono, especialidad) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (numero_documento, nombre, apellido, email, telefono, especialidad)
            ejecutar_consulta(conexion, consulta, valores)
            confirmar_cambios(conexion)
    finally:
        cerrar_db(conexion)

def buscarTodos():
    """Buscar todos los docentes."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "SELECT * FROM docentes"
            resultados = ejecutar_consulta(conexion, consulta)
            return resultados
    finally:
        cerrar_db(conexion)

def buscarPorDocumento(numero_documento):
    """Buscar un docente por número de documento."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "SELECT * FROM docentes WHERE numero_documento = %s"
            valores = (numero_documento,)
            resultados = ejecutar_consulta(conexion, consulta, valores)
            if resultados:
                return resultados[0]
            else:
                return None
    finally:
        cerrar_db(conexion)

def actualizar(numero_documento, nombre, apellido, email, telefono, especialidad):
    """Actualizar un docente existente."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "UPDATE docentes SET nombre = %s, apellido = %s, email = %s, telefono = %s, especialidad = %s WHERE numero_documento = %s"
            valores = (nombre, apellido, email, telefono, especialidad, numero_documento)
            ejecutar_consulta(conexion, consulta, valores)
            confirmar_cambios(conexion)
    finally:
        cerrar_db(conexion)

def eliminar(numero_documento):
    """Eliminar un docente por número de documento."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "DELETE FROM docentes WHERE numero_documento = %s"
            valores = (numero_documento,)
            ejecutar_consulta(conexion, consulta, valores)
            confirmar_cambios(conexion)
    finally:
        cerrar_db(conexion)