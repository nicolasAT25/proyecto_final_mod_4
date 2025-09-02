from prettytable import PrettyTable

def show_tacher(teacher):
    """Muestra la información de un docente."""
    table = PrettyTable()
    table.field_names = ["Número de documento", "Nombre", "Apellido", "Email", "Teléfono", "Especialidad"]
    table.add_row([teacher["numero_documento"], teacher["nombre"], teacher["apellido"], teacher["email"], teacher["telefono"], teacher["especialidad"]])
    print(table)

def mostrar_docentes(teachers):
    """Muestra la lista de docentes."""
    table = PrettyTable()
    table.field_names = ["Número de documento", "Nombre", "Apellido", "Email", "Teléfono", "Especialidad"]
    for teacher in teachers:
        table.add_row([teacher["numero_documento"], teacher["nombre"], teacher["apellido"], teacher["email"], teacher["telefono"], teacher["especialidad"]])
    print(table)
