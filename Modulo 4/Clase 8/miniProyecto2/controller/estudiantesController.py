from models import estudiantesModel
from views import estudiantesView

def mostrar_estudiante(numero_documento):
    """Mostrar los datos de un estudiante."""
    estudiante = estudiantesModel.buscarPorDocumento(numero_documento)
    if estudiante:
        estudiantesView.mostrar_estudiante(estudiante)
    else:
        print("Estudiante no encontrado.")

def mostar_estudiantes():
    """Mostrar la lista de estudiantes."""
    estudiantes = estudiantesModel.buscarTodos()
    if estudiantes:
        estudiantesView.mostrar_estudiantes(estudiantes)
    else:
        print("No hay estudiantes registrados.")

def crear_estudiante(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono):
    """Crear un nuevo estudiante."""
    estudiantesModel.crear(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
    print("Estudiante creado exitosamente.")

def modificar_estudiante(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono):
    """Modificar un estudiante existente."""
    estudiantesModel.actualizar(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
    print("Estudiante modificado exitosamente.")

def eliminar_estudiante(numero_documento):
    """Eliminar un estudiante por número de documento."""
    estudiantesModel.eliminar(numero_documento)
    print("Estudiante eliminado exitosamente.")