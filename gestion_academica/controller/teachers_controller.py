from models import teachers_model
from views import teachers_view

def show_teacher(numero_documento):
    """Mostrar los datos de un docente."""
    teacher = teachers_model.read_teacher_by_document(numero_documento)
    if teacher:
        teachers_view.show_tacher(teacher)
    else:
        print("Docente no encontrado.")

def show_teachers():
    """Mostrar la lista de docentes."""
    tachers = teachers_model.read_teachers()
    if tachers:
        teachers_view.mostrar_docentes(tachers)
    else:
        print("No hay docentes registrados.")

def create_teacher(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono):
    """Crear un nuevo docente."""
    teachers_model.create_teacher(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
    print("Docente creado exitosamente.")

def update_teacher(numero_documento):
    """Modificar un docente existente."""
    teachers_model.update_teacher(numero_documento)
    print("Docente modificado exitosamente.")

def delete_teacher(numero_documento):
    """Eliminar un docente por número de documento."""
    teachers_model.delete_teacher(numero_documento)
    print("Docente eliminado exitosamente.")