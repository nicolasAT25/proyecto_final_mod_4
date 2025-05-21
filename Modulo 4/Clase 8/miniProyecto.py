import mysql.connector
from mysql.connector import Error

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

# Estudiantes
def listar_estudiantes(conexion): 
    """Listar todos los estudiantes."""
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM estudiantes")
        estudiantes = cursor.fetchall()
        print("Lista de estudiantes:")
        for estudiante in estudiantes:
            print(estudiante)
    except Error as err:
        print(f"Error al listar estudiantes: {err}")
    finally:
        cursor.close()

def agregar_estudiante(conexion, numeroDocumento, nombre, apellido, fechaNacimiento, email, telefono):
    """Agregar un nuevo estudiante."""
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO estudiantes (numero_documento, nombre, apellido, fecha_nacimiento, email, telefono) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (numeroDocumento, nombre, apellido, fechaNacimiento, email, telefono))
        conexion.commit()
        print("Estudiante agregado exitosamente")
    except Error as err:
        print(f"Error al agregar estudiante: {err}")
    finally:
        cursor.close()

def buscar_estudiante(conexion, numeroDocumento):
    """Buscar un estudiante por número de documento."""
    try:
        cursor = conexion.cursor()
        sql = "SELECT * FROM estudiantes WHERE numero_documento = %s"
        cursor.execute(sql, (numeroDocumento,))
        estudiante = cursor.fetchone()
        if estudiante:
            print("Estudiante encontrado:", estudiante)
        else:
            print("Estudiante no encontrado")
    except Error as err:
        print(f"Error al buscar estudiante: {err}")
    finally:
        cursor.close()

def actualizar_estudiante(conexion, numeroDocumento, nombre, apellido, fechaNacimiento, email, telefono):
    """Actualizar un estudiante existente."""
    try:
        cursor = conexion.cursor()
        sql = "UPDATE estudiantes SET nombre = %s, apellido = %s, fecha_nacimiento = %s, email = %s, telefono = %s WHERE numero_documento = %s"
        cursor.execute(sql, (nombre, apellido, fechaNacimiento, email, telefono, numeroDocumento))
        conexion.commit()
        print("Estudiante actualizado exitosamente")
    except Error as err:
        print(f"Error al actualizar estudiante: {err}")
    finally:
        cursor.close()

def eliminar_estudiante(conexion, numeroDocumento):
    """Eliminar un estudiante por número de documento."""
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM estudiantes WHERE numero_documento = %s"
        cursor.execute(sql, (numeroDocumento,))
        conexion.commit()
        print("Estudiante eliminado exitosamente")
    except Error as err:
        print(f"Error al eliminar estudiante: {err}")
    finally:
        cursor.close()



def menu_estudiantes(conexion):
    while True:
        print("\nMenu de estudiantes:")
        print("1. Listar estudiantes")
        print("2. Agregar estudiante")
        print("3. Buscar estudiante")
        print("4. Actualizar estudiante")
        print("5. Eliminar estudiante")
        print("6. Salir")

        opcion = input("Seleccione una opcción: ")

        if opcion == "1":
            listar_estudiantes(conexion)
        elif opcion == "2":
            numeroDocumento = input("Ingrese el número de documento: ")
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            fechaNacimiento = input("Ingrese la fecha de nacimiento(formato AAAA-MM-DD): ")
            email = input("Ingrese el correo electrónica: ")
            telefono = input("Ingrese el teléfono: ")
            agregar_estudiante(conexion, numeroDocumento, nombre, apellido, fechaNacimiento, email, telefono)
        elif opcion == "3":
            numeroDocumento = input("Ingrese el número de documento: ")
            buscar_estudiante(conexion, numeroDocumento)
        elif opcion == "4":
            numeroDocumento = input("Ingrese el número de documento: ")
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            fechaNacimiento = input("Ingrese la nueva fecha de nacimiento(formato AAAA-MM-DD): ")
            email = input("Ingrese el nuevo correo electrónico: ")
            telefono = input("Ingrese el nuevo teléfono: ")
            actualizar_estudiante(conexion, numeroDocumento, nombre, apellido, fechaNacimiento, email, telefono)
        elif opcion == "5":
            numeroDocumento = input("Ingrese el número de documento: ")
            eliminar_estudiante(conexion, numeroDocumento)
        elif opcion == "6":
            print("Saliendo del menú de estudiantes.")
            break

menu_estudiantes(conectar_db())