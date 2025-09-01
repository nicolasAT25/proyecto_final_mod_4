from prettytable import PrettyTable

def mostrar_estudiante(estudiante):
    """Mostrar los datos de un estudiante."""
    tabla = PrettyTable()
    tabla.field_names = ["Número de documento", "Nombre", "Apellido", "Fecha de nacimiento", "Email", "Teléfono"]
    tabla.add_row([estudiante["numero_documento"], estudiante["nombre"], estudiante["apellido"], estudiante["fecha_nacimiento"], estudiante["email"], estudiante["telefono"]])
    print(tabla)

def mostrar_estudiantes(estudiantes):
    """Mostrar la lista de estudiantes."""
    tabla = PrettyTable()
    tabla.field_names = ["Número de documento", "Nombre", "Apellido", "Fecha de nacimiento", "Email", "Teléfono"]
    for estudiante in estudiantes:
        tabla.add_row([estudiante["numero_documento"], estudiante["nombre"], estudiante["apellido"], estudiante["fecha_nacimiento"], estudiante["email"], estudiante["telefono"]])
    print(tabla)


