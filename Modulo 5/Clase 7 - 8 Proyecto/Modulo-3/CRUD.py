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

    def cerrar_conexion(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion_recomendada2:
            self.conexion_recomendada2.close()
        print("Conexión cerrada")

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
        finally:
            self.cerrar_conexion()

    def aumento_salario(self):
        try:
            with self.conexion_recomendada2:
                with self.cursor as cur:
                    cur.execute("UPDATE empleados SET salario = salario * 1.10 WHERE id = 'b63227ea-908e-437d-bb75-81a3b47c289b'")
                    cur.execute("UPDATE empleados SET salario = salario * 1.10 WHERE id = d531a5e9-c296-46fb-bc65-82399d2e2cba")

            print("Aumento de salario exitoso")
        except Exception as e:
            print("Error al aumentar el salario:", e)
        finally:
            self.cerrar_conexion()

    def insertar_empleado(self, nombre, puesto, salario):
        try:
            with self.conexion_recomendada2:
                with self.cursor as cur:
                    #No recomiendo usar interpolación de cadenas directamente en consultas SQL por razones de seguridad (inyección SQL).
                    '''
                    cur.execute(f"INSERT INTO empleados (nombre, puesto, salario) VALUES (${nombre}, ${puesto}, ${salario})")
                    '''

                    cur.execute(
                        "INSERT INTO empleados (nombre, puesto, salario) VALUES (%s, %s, %s)",
                        (nombre, puesto, salario)
                    )
            print("Empleado insertado exitosamente")
        except Exception as e:
            print("Error al insertar empleado:", e)
        finally:
            self.cerrar_conexion()
            


        


mi_conexion = DatabaseConnection()
mi_conexion.consultar_empleados()