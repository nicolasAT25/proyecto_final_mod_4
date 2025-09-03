# import mysql.connector

# # Detalles de la conexión
# db_config = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'admin',
#     'database': 'academia',
#     'port': 3306
# }

# # Conexión a la base de datos
# def conectar_db():
#     """Establece la conexión a la base de datos y devuelve el objeto de conexión."""
#     try:
#         conexion = mysql.connector.connect(**db_config)
#         if conexion.is_connected():
#             print("Conexión exitosa a la base de datos")
#             return conexion
#     except mysql.connector.Error as err:
#         print(f"Error de conexión: {err}")
#         return None
    
# # Cierre de la conexión
# def cerrar_db(conexion):
#     """Cierra la conexión a la base de datos."""
#     if conexion.is_connected():
#         conexion.close()
#         print("Conexión cerrada")

# # ejecutar consulta
# def ejecutar_consulta(conexion, consulta, params=None):
#     """Ejecuta una consulta SQL y devuelve los resultados."""
#     try:
#         cursor = conexion.cursor()
#         cursor.execute(consulta, params)
#         resultados = cursor.fetchall()
#         return resultados
#     except mysql.connector.Error as err:
#         print(f"Error al ejecutar consulta: {err}")
#         return None
#     finally:
#         cursor.close()

# def confirmar_cambios(conexion):
#     """Confirma los cambios en la base de datos."""
#     try:
#         conexion.commit()
#         print("Cambios confirmados")
#     except mysql.connector.Error as err:
#         print(f"Error al confirmar cambios: {err}")
        
###############

import psycopg
from psycopg.rows import dict_row
import time
from config import settings

# Conexión a la base de datos
def db_connect():
    """Establece la conexión a la base de datos y devuelve el objeto de conexión."""
    while True:
        try:
            conn = psycopg.connect(
                host=settings.database_hostname, 
                dbname=settings.database_name, 
                user=settings.database_username, 
                password=settings.database_password, 
                port=settings.database_port,
                row_factory=dict_row
                )
            
            # cursor = conn.cursor()
            print('Conexión a la base de datos exitosa!')
            break
        
        except psycopg.errors.ConnectionException as e:
            print(f'Conexión a la base de datos fallida. Error: {e}')
            time.sleep(2)
            
    return conn

# Cierre de la conexión
def close_db_conn(conn):
    """Cierra la conexión a la base de datos."""
    if conn.closed == False:
        conn.close()
        print("Conexión cerrada")
        
# ejecutar consulta
def execute_query(conn, query, params=None):
    """Ejecuta una consulta SQL y devuelve los resultados."""
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        res = cursor.fetchall()
        return res
    
    except psycopg.errors.QueryCanceled as e:
        print(f"Error al ejecutar consulta: {e}")
        
    except Exception as e:
        print(f"Error inesperado: {e}")
    
    finally:
        cursor.close()
        
def commit_changes(conn):
    """Confirma los cambios en la base de datos."""
    try:
        conn.commit()
        print("Cambios confirmados")
    except psycopg.errors.ConnectionException as e:
        print(f"Error al confirmar cambios: {e}")