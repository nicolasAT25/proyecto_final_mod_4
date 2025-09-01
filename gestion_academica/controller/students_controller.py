from models import students_model
from views import students_view

def mostrar_estudiante(numero_documento):
    """Mostrar los datos de un estudiante."""
    estudiante = students_model.read_student_by_document(numero_documento)
    if estudiante:
        students_view.mostrar_estudiante(estudiante)
    else:
        print("Estudiante no encontrado.")

def mostar_estudiantes():
    """Mostrar la lista de estudiantes."""
    estudiantes = students_model.read_students()
    if estudiantes:
        print(estudiantes)
        students_view.mostrar_estudiantes(estudiantes)
    else:
        print("No hay estudiantes registrados.")

def crear_estudiante(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono):
    """Crear un nuevo estudiante."""
    students_model.create_student(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
    print("Estudiante creado exitosamente.")

def modificar_estudiante(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono):
    """Modificar un estudiante existente."""
    students_model.update_student(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
    print("Estudiante modificado exitosamente.")

def eliminar_estudiante(numero_documento):
    """Eliminar un estudiante por número de documento."""
    students_model.delete_student(numero_documento)
    print("Estudiante eliminado exitosamente.")