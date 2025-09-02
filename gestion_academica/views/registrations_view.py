from prettytable import PrettyTable

def show_registrations(inscripciones):
    """Mostrar los datos de una inscripciónes."""
    table = PrettyTable()
    table.title = "Inscripciones"
    table.field_names = ["ID Inscripción", "Número de documento", "Nombre Estudiante", "ID Curso", "Nombre Curso", "Fecha Inscripción"]
    for inscripcion in inscripciones:
        table.add_row([inscripcion["id_inscripcion"], inscripcion["numero_documento"], f"{inscripcion["nombre"]} {inscripcion["apellido"]}", inscripcion["id_curso"], inscripcion["nombre_curso"], inscripcion["fecha_inscripcion"]])
    print(table)
   
def show_registration_by_id(registration):
    """Muestra la información de un curso por el id del docente."""
    table = PrettyTable()
    table.field_names = ["ID Estudiante", "ID Curso", "Fecha Inscripción"]
    table.add_row([registration["id_estudiante"], registration["id_curso"], registration["fecha_inscripcion"]])
    print(table)