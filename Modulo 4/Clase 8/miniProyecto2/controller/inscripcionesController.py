from models import inscripcionModel
from views import inscripcionView

def mostrar_inscripciones():
    inscripcion = inscripcionModel.consultarInscripciones()
    if inscripcion:
        inscripcionView.mostar_inscripciones(inscripcion)
    else:
        print("No hay inscripciones registradas.")