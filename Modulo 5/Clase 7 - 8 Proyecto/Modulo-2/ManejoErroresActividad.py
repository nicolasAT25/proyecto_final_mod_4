import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseConnection():
    def __init__(self):
        self.BD_NAME = os.getenv("DB_NAME")
        self.BD_USER = os.getenv("DB_USER")
        self.BD_PASS = os.getenv("DB_PASS")
        self.BD_HOST = os.getenv("DB_HOST")
        self.BD_PORT = os.getenv("DB_PORT")
        try:
            self.conexion_recomendada2 = psycopg2.connect(
                host=self.BD_HOST, 
                database=self.BD_NAME, 
                user=self.BD_USER, 
                password=self.BD_PASS, 
                port=self.BD_PORT
            )

            self.cursor = self.conexion_recomendada2.cursor()

            if self.conexion_recomendada2:
                print("Conexión exitosa a la base de datos")
        except psycopg2.OperationalError as e:
            print(f"Error de conexión a la base de datos: {e}")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")

    def consultar_empleados(self):
        try:
            select_query = "SELECT * FROM empleados"
            print("Consulta a la base de datos:")
            self.cursor.execute(select_query)
            empleados = self.cursor.fetchall()
            for empleado in empleados:
                print(empleado)
        except psycopg2.ProgrammingError as e:
            print(f"Error en la consulta SQL: {e}")
        except Exception as e:
            print(f"Error al consultar empleados: {e}")

mi_conexion = DatabaseConnection()
mi_conexion.consultar_empleados()
