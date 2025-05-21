from database import conectar_db, cerrar_db, ejecutar_consulta, confirmar_cambios

def crear(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono):
    """Crear un nuevo estudiante."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "INSERT INTO estudiantes (numero_documento, nombre, apellido, fecha_nacimiento, email, telefono) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
            ejecutar_consulta(conexion, consulta, valores)
            confirmar_cambios(conexion)
    finally:
        cerrar_db(conexion)

def buscarTodos():
    """Buscar todos los estudiantes."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "SELECT * FROM estudiantes"
            resultados = ejecutar_consulta(conexion, consulta)
            return resultados
    finally:
        cerrar_db(conexion)

def buscarPorDocumento(numero_documento):
    """Buscar un estudiante por número de documento."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "SELECT * FROM estudiantes WHERE numero_documento = %s"
            valores = (numero_documento,)
            resultados = ejecutar_consulta(conexion, consulta, valores)
            if resultados:
                return resultados[0]
            else:
                return None
    finally:
        cerrar_db(conexion)

def actualizar(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono):
    """Actualizar un estudiante existente."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "UPDATE estudiantes SET nombre = %s, apellido = %s, fecha_nacimiento = %s, email = %s, telefono = %s WHERE numero_documento = %s"
            valores = (nombre, apellido, fecha_nacimiento, email, telefono, numero_documento)
            ejecutar_consulta(conexion, consulta, valores)
            confirmar_cambios(conexion)
    finally:
        cerrar_db(conexion)

def eliminar(numero_documento):
    """Eliminar un estudiante por número de documento."""
    try:
        conexion = conectar_db()
        if conexion:
            consulta = "DELETE FROM estudiantes WHERE numero_documento = %s"
            valores = (numero_documento,)
            ejecutar_consulta(conexion, consulta, valores)
            confirmar_cambios(conexion)
    finally:
        cerrar_db(conexion)