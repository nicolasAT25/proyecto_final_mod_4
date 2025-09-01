from models import registrations_model
from views import registrations_view

def mostrar_inscripciones():
    inscripcion = registrations_model.read_inscriptions()
    if inscripcion:
        registrations_view.mostar_inscripciones(inscripcion)
    else:
        print("No hay inscripciones registradas.")