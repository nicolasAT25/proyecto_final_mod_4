from prettytable import PrettyTable

def show_student(estudiante):
    """Mostrar los datos de un estudiante."""
    table = PrettyTable()
    table.field_names = ["Número de documento", "Nombre", "Apellido", "Fecha de nacimiento", "Email", "Teléfono"]
    table.add_row([estudiante["numero_documento"], estudiante["nombre"], estudiante["apellido"], estudiante["fecha_nacimiento"], estudiante["email"], estudiante["telefono"]])
    print(table)

def show_students(estudiantes):
    """Mostrar la lista de estudiantes."""
    table = PrettyTable()
    table.field_names = ["Número de documento", "Nombre", "Apellido", "Fecha de nacimiento", "Email", "Teléfono"]
    for estudiante in estudiantes:
        table.add_row([estudiante["numero_documento"], estudiante["nombre"], estudiante["apellido"], estudiante["fecha_nacimiento"], estudiante["email"], estudiante["telefono"]])
    print(table)


