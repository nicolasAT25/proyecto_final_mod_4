from prettytable import PrettyTable

def mostrar_estudiante(estudiante):
    """Mostrar los datos de un estudiante."""
    tabla = PrettyTable()
    tabla.field_names = ["Número de documento", "Nombre", "Apellido", "Fecha de nacimiento", "Email", "Teléfono"]
    tabla.add_row([estudiante[1], estudiante[2], estudiante[3], estudiante[4], estudiante[5], estudiante[6]])
    print(tabla)

def mostrar_estudiantes(estudiantes):
    """Mostrar la lista de estudiantes."""
    tabla = PrettyTable()
    tabla.field_names = ["Número de documento", "Nombre", "Apellido", "Fecha de nacimiento", "Email", "Teléfono"]
    for estudiante in estudiantes:
        tabla.add_row([estudiante[1], estudiante[2], estudiante[3], estudiante[4], estudiante[5], estudiante[6]])
    print(tabla)


