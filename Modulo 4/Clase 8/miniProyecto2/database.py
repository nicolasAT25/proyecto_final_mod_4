import mysql.connector

# Detalles de la conexión
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',
    'database': 'academia',
    'port': 3306
}

# Conexión a la base de datos
def conectar_db():
    """Establece la conexión a la base de datos y devuelve el objeto de conexión."""
    try:
        conexion = mysql.connector.connect(**db_config)
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None
    
# Cierre de la conexión
def cerrar_db(conexion):
    """Cierra la conexión a la base de datos."""
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")

# ejecutar consulta
def ejecutar_consulta(conexion, consulta, params=None):
    """Ejecuta una consulta SQL y devuelve los resultados."""
    try:
        cursor = conexion.cursor()
        cursor.execute(consulta, params)
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as err:
        print(f"Error al ejecutar consulta: {err}")
        return None
    finally:
        cursor.close()

def confirmar_cambios(conexion):
    """Confirma los cambios en la base de datos."""
    try:
        conexion.commit()
        print("Cambios confirmados")
    except mysql.connector.Error as err:
        print(f"Error al confirmar cambios: {err}") 