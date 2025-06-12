import psycopg2

#Establecer la conexión con la base de datos
conexion = psycopg2.connect(
    host="localhost", # Por defecto es localhost 127.0.0.1
    database="Academia", # Nombre de la base de datos
    user="postgres", # Por defecto es postgres
    password="Admin", # Por defecto es admin
    port="5432" # Por defecto es 5432
)

#Crear un cursor
cursor = conexion.cursor()

#Insertar datos
insert_query = """
INSERT INTO empleados (nombre, puesto, salario) VALUES (%s, %s, %s)
"""
nombre = input("Ingrese el nombre del empleado: ")
puesto = input("Ingrese el puesto del empleado: ")
salario = input("Ingrese el salario del empleado: ")

empleado_datos = (nombre, puesto, salario)

cursor.execute(insert_query, empleado_datos)
conexion.commit()