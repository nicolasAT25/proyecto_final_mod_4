from prettytable import PrettyTable

def mostar_inscripciones(inscripcion):
    """Mostrar los datos de una inscripciónes."""
    tabla = PrettyTable()
    tabla.title = "Inscripciones"
    tabla.field_names = ["ID Inscripción", "Número de documento", "Nombre Estudiante", "ID Curso", "Nombre Curso", "Fecha Inscripción"]
    for inscripcion in inscripcion:
        tabla.add_row([inscripcion[0], inscripcion[1], f"{inscripcion[2]} {inscripcion[3]}", inscripcion[4], inscripcion[5], inscripcion[6]])
    print(tabla)
   