from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from prettytable import PrettyTable

# Configuración de la base de datos
engine = create_engine("sqlite:///./relational_tareas.db", echo=True)

# Declarative base
Base = declarative_base()

# Definición de la tabla
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True)
    
    tareas = relationship("Tarea", back_populates="usuario")

class Tarea(Base):
    __tablename__ = "tareas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(200), default=False)
    completada = Column(Boolean, default=False)

    usuario_id = Column(Integer, ForeignKey('usuarios.id'))

    usuario = relationship("Usuario", back_populates="tareas")

    def __repr__(self):
        estado = "[X]" if self.completada else "[ ]"
        return f"Tarea(id={self.id}, nombre='{self.nombre}', descripcion='{self.descripcion}', estado='{estado}')"

# Crear la tabla en la base de datos
Base.metadata.create_all(engine)
# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()

# Crear un nuevo usuario
def crear_usuario(nombre):
    # Verificar si el usuario ya existe
    usuario_existente = session.query(Usuario).filter_by(nombre=nombre).first()
    if usuario_existente:
        print(f"El usuario '{nombre}' ya existe.")
        return
    nuevo_usuario = Usuario(nombre=nombre)
    session.add(nuevo_usuario)
    session.commit()
    print(f"Usuario '{nombre}' creado con éxito.")

# Crear una nueva tarea
def crear_tarea(usuario_id, descripcion):
    nueva_tarea = Tarea(usuario_id=usuario_id, descripcion=descripcion)
    session.add(nueva_tarea)
    session.commit()
    print(f"Tarea '{descripcion}' creada con éxito para el usuario con ID {usuario_id}.")

def listar_usuarios_y_sus_tareas():
    table = PrettyTable()
    table.field_names = ["ID Usuario", "Nombre Usuario", "ID Tarea", "Descripción", "Estado"]
    table.title = "Lista de Usuarios y sus Tareas"

    usuarios = session.query(Usuario).all()
    if usuarios:
        for usuario in usuarios:
            for tarea in usuario.tareas:
                estado = "[X]" if tarea.completada else "[ ]"
                table.add_row([usuario.id, usuario.nombre, tarea.id, tarea.descripcion, estado])
        print(table)
    else:
        print("No hay usuarios en la base de datos.")

def listar_todas_las_tareas():
    table = PrettyTable()
    table.field_names = ["ID Tarea", "Descripción", "Estado"]
    table.title = "Lista de Tareas"

    tareas = session.query(Tarea).all()
    if tareas:
        for tarea in tareas:
            estado = "[X]" if tarea.completada else "[ ]"
            table.add_row([tarea.id, tarea.descripcion, estado])
        print(table)
    else:
        print("No hay tareas en la base de datos.")

def marcar_tarea_completada(tarea_id):
    tarea = session.query(Tarea).filter_by(id=tarea_id).first()
    if tarea:
        tarea.completada = True
        session.commit()
        print(f"Tarea '{tarea.descripcion}' marcada como completada.")
    else:
        print(f"No se encontró la tarea con ID {tarea_id}.")

def menu():
    print("Bienvenido al gestor de tareas.")
    print("1. Crear usuario")
    print("2. Crear tarea")
    print("3. Listar usuarios y sus tareas")
    print("4. Listar todas las tareas")
    print("5. Marcar tarea como completada")
    print("6. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre del usuario: ")
            crear_usuario(nombre)
        elif opcion == "2":
            usuario_id = int(input("Ingrese el ID del usuario: "))
            descripcion = input("Ingrese la descripción de la tarea: ")
            crear_tarea(usuario_id, descripcion)
        elif opcion == "3":
            listar_usuarios_y_sus_tareas()
        elif opcion == "4":
            listar_todas_las_tareas()
        elif opcion == "5":
            tarea_id = int(input("Ingrese el ID de la tarea a marcar como completada: "))
            marcar_tarea_completada(tarea_id)
        elif opcion == "6":
            print("Saliendo del gestor de tareas.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()