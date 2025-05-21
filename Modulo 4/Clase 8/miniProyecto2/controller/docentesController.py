from models import docentesModel
from views import docentesView

def mostrar_docente(numero_documento):
    """Mostrar los datos de un docente."""
    docente = docentesModel.buscarPorDocumento(numero_documento)
    if docente:
        docentesView.mostrar_docente(docente)
    else:
        print("Docente no encontrado.")

def mostrar_docentes():
    """Mostrar la lista de docentes."""
    docentes = docentesModel.buscarTodos()
    if docentes:
        docentesView.mostrar_docentes(docentes)
    else:
        print("No hay docentes registrados.")

def crear_docente(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono):
    """Crear un nuevo docente."""
    docentesModel.crear(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
    print("Docente creado exitosamente.")

def modificar_docente(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono):
    """Modificar un docente existente."""
    docentesModel.actualizar(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
    print("Docente modificado exitosamente.")

def eliminar_docente(numero_documento):
    """Eliminar un docente por número de documento."""
    docentesModel.eliminar(numero_documento)
    print("Docente eliminado exitosamente.")