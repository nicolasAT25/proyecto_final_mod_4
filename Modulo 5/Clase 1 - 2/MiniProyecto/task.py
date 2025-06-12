from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

from prettytable import PrettyTable

# Configuración de la base de datos
engine = create_engine("sqlite:///./tareas.db", echo=True)

# Declarative base
Base = declarative_base()

# Definición de la tabla
class Tarea(Base):
    __tablename__ = "tareas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    descripcion = Column(String(200), default=False)
    completada = Column(Boolean, default=False)

    def __repr__(self):
        estado = "Completada" if self.completada else "No completada"
        return f"Tarea(id={self.id}, nombre='{self.nombre}', descripcion='{self.descripcion}', estado='{estado}')"    
# Crear la tabla en la base de datos
Base.metadata.create_all(engine)  

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crear una nueva terea
def crear_tarea(nombre, descripcion):
    nueva_tarea = Tarea(nombre=nombre, descripcion=descripcion)
    session.add(nueva_tarea)  
    session.commit()  # Guardar los cambios en la base de datos
    print(f"Tarea '{nombre}' creada con éxito.")

def listar_tareas():

    table = PrettyTable()
    table.field_names = ["ID", "Nombre", "Descripción", "Estado"]
    table.title = "Lista de Tareas"

    tareas = session.query(Tarea).all()
    if tareas:
        for tarea in tareas:
            estado = "Completada" if tarea.completada else "No completada"
            table.add_row([tarea.id, tarea.nombre, tarea.descripcion, estado])
        print(table)
    else:
        print("No hay tareas en la base de datos.")
        
def buscar_tarea(id):
    
    table = PrettyTable()
    table.field_names = ["ID", "Nombre", "Descripción", "Estado"]
    table.title = "Tarea Encontrada"

    tarea = session.query(Tarea).filter_by(id=id).first()
    if tarea:
        estado = "Completada" if tarea.completada else "No completada"
        table.add_row([tarea.id, tarea.nombre, tarea.descripcion, estado])
        print(table)
    else:
        print(f"No se encontró la tarea con ID {id}.")

def completar_tarea(id):
    tarea = session.query(Tarea).filter_by(id=id).first()
    if tarea:
        tarea.completada = True
        session.commit()
        print(f"Tarea '{tarea.nombre}' marcada como completada.")
    else:
        print(f"No se encontró la tarea con ID {id}.")

def menu():
    print("Bienvenido al gestor de tareas.")
    print("1. Crear tarea")
    print("2. Listar tareas")
    print("3. Buscar tarea")
    print("4. Completar tarea")
    print("5. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            crear_tarea(nombre, descripcion)
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            id = int(input("Ingrese el ID de la tarea a buscar: "))
            buscar_tarea(id)
        elif opcion == "4":
            id = int(input("Ingrese el ID de la tarea a completar: "))
            completar_tarea(id)
        elif opcion == "5":
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()