from models import teachers_model
from views import teachers_view

def mostrar_docente(numero_documento):
    """Mostrar los datos de un docente."""
    docente = teachers_model.read_teacher_by_document(numero_documento)
    if docente:
        teachers_view.mostrar_docente(docente)
    else:
        print("Docente no encontrado.")

def mostrar_docentes():
    """Mostrar la lista de docentes."""
    docentes = teachers_model.read_teachers()
    if docentes:
        teachers_view.mostrar_docentes(docentes)
    else:
        print("No hay docentes registrados.")

def crear_docente(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono):
    """Crear un nuevo docente."""
    teachers_model.create_teacher(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
    print("Docente creado exitosamente.")

def modificar_docente(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono):
    """Modificar un docente existente."""
    teachers_model.update_teacher(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
    print("Docente modificado exitosamente.")

def eliminar_docente(numero_documento):
    """Eliminar un docente por número de documento."""
    teachers_model.delete_teacher(numero_documento)
    print("Docente eliminado exitosamente.")