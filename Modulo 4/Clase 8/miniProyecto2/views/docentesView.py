from prettytable import PrettyTable

def mostrar_docente(docente):
    """Muestra la información de un docente."""
    tabla = PrettyTable()
    tabla.field_names = ["Número de documento", "Nombre", "Apellido", "Email", "Teléfono", "Especialidad"]
    tabla.add_row([docente[1], docente[2], docente[3], docente[4], docente[5], docente[6]])
    print(tabla)

def mostrar_docentes(docentes):
    """Muestra la lista de docentes."""
    tabla = PrettyTable()
    tabla.field_names = ["Número de documento", "Nombre", "Apellido", "Email", "Teléfono", "Especialidad"]
    for docente in docentes:
        tabla.add_row([docente[1], docente[2], docente[3], docente[4], docente[5], docente[6]])
    print(tabla)
