import mysql.connector

# Detalles de la conexión
cnx = mysql.connector.connect(
    host="localhost", # Es lo mismo que 127.0.0.1
    user="root", # Usuario por defecto
    password="admin", # Contraseña por defecto
    database="academia", # Nombre de la base de datos
    port=3306 # Puerto por defecto
)
# Conexión a la base de datos

cur = cnx.cursor()

# crear un ping de conexión
def ping():
    try:
        cur.execute("SELECT 1")
        print("Conexión exitosa")
    except e as e:
        print("Error de conexión:", e)

# Ejecutar el ping
ping()

# Cerrar el cursor y la conexión
cur.close()
cnx.close()