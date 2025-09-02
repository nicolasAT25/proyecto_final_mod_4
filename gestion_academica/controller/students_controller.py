from models import students_model
from views import students_view

def show_student(numero_documento):
    """Mostrar los datos de un estudiante."""
    estudiante = students_model.read_student_by_document(numero_documento)
    if estudiante:
        students_view.show_student(estudiante)
    else:
        print("Estudiante no encontrado.")

def show_students():
    """Mostrar la lista de estudiantes."""
    estudiantes = students_model.read_students()
    if estudiantes:
        students_view.show_students(estudiantes)
    else:
        print("No hay estudiantes registrados.")

def create_student(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono):
    """Crear un nuevo estudiante."""
    students_model.create_student(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
    print("Estudiante creado exitosamente.")

def update_student(numero_documento):
    """Modificar un estudiante existente."""
    students_model.update_student_by_document(numero_documento)
    print("Estudiante modificado exitosamente.")

def delete_student(numero_documento):
    """Eliminar un estudiante por número de documento."""
    students_model.delete_student(numero_documento)
    print("Estudiante eliminado exitosamente.")