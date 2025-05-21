import mysql.connector

# Detalles de la conexión
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',
    'database': 'seguridad',
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
    
def login(username, password):
    conexion = conectar_db()
    cursor = conexion.cursor()
    consulta = f"SELECT * FROM usuarios WHERE username = '{username}' AND password = '{password}'"
    print(f"Consulta construida: {consulta}")
    cursor.execute(consulta)
    resultado = cursor.fetchone()
    if resultado:
        print("Inicio de sesión exitoso")
        return True
    else:
        print("Credenciales incorrectas")
        return False
# Ejemplo de uso
if __name__ == "__main__":
    username = ""
    password = "admin ' OR '1'='1"
    login(username, password)