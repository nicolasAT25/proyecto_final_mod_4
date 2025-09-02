from models import registrations_model
from views import registrations_view

def create_course(id_estudiante, id_curso, fecha_inscripcion):
    """Crear una nueva inscripción."""
    registrations_model.create_registration(id_estudiante, id_curso, fecha_inscripcion)
    print("Inscripción creada exitosamente.")

def show_registrations():
    inscripcion = registrations_model.read_registrations()
    if inscripcion:
        registrations_view.show_registrations(inscripcion)
    else:
        print("No hay inscripciones registradas.")
        
def show_registration(id_inscripcion):
    """Mostrar los datos de una inscripción."""
    inscripcion = registrations_model.read_inscription_by_id(id_inscripcion)
    if inscripcion:
        registrations_view.show_registration_by_id(inscripcion)
    else:
        print("Inscripción no encontrada.")
        
def update_registration(id_inscripcion):
    """Modificar una inscripción existente."""
    registrations_model.update_registration_by_id(id_inscripcion)
    print("Inscripción modificada exitosamente.")
    
def delete_registration(id_inscripcion):
    """Eliminar un estudiante por número de documento."""
    registrations_model.delete_registration(id_inscripcion)
    print("Inscripción eliminada exitosamente.")