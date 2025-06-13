import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

try:

    BD_NAME = os.getenv("DB_NAME")
    BD_USER = os.getenv("DB_USER")
    BD_PASS = os.getenv("DB_PASS")
    BD_HOST = os.getenv("DB_HOST")
    BD_PORT = os.getenv("DB_PORT")

    conexion_recomendada2 = psycopg2.connect(
        host=BD_HOST, 
        database=BD_NAME, 
        user=BD_USER, 
        password=BD_PASS, 
        port=BD_PORT
    )

    cursor = conexion_recomendada2.cursor()

    if conexion_recomendada2:
        print("Conexión exitosa a la base de datos")

except psycopg2.OperationalError as e:
    print(f"Error de conexión a la base de datos: {e}")
    
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")


#consulta
select_query = """
SELECT * FROM empleados
"""

print("Consulta a la base de datos:")
empleados = cursor.execute(select_query)
for empleado in cursor.fetchall():
    print(empleado)