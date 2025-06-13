import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

BD_NAME = os.getenv("DB_NAME")
BD_USER = os.getenv("DB_USER")
BD_PASS = os.getenv("DB_PASS")
BD_HOST = os.getenv("DB_HOST")
BD_PORT = os.getenv("DB_PORT")

#Establecer la conexión con la base de datos (NO RECIBIR DATOS DEL USUARIO)
conexion = psycopg2.connect(
    host="localhost", 
    database="Academia", 
    user="postgres", 
    password="Admin", 
    port="5432" 
)

#Establecer la conexión con la base de datos (RECIBIR DATOS DEL USUARIO)
conexion_recomendada = psycopg2.connect(
    host=BD_HOST, 
    database=BD_NAME, 
    user=BD_USER, 
    password=BD_PASS, 
    port=BD_PORT
)

#Establecer la conexión con la base de datos (RECIBIENDO DATOS DEL USUARIO) implementando try

conexion_recomendada2 = psycopg2.connect(
    host=BD_HOST, 
    database=BD_NAME, 
    user=BD_USER, 
    password=BD_PASS, 
    port=BD_PORT
)


#Crear un cursor
cursor = conexion_recomendada.cursor()

#Consultar datos
select_query = """
SELECT * FROM empleados
"""

cursor.execute(select_query)
empleados = cursor.fetchall()

for empleado in empleados:
    print(empleado)