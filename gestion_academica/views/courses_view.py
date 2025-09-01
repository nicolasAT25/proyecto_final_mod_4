from prettytable import PrettyTable

def mostrar_cursos(cursos):
    """Muestra la información de un curso."""
    tabla = PrettyTable()
    tabla.title = "Cursos"
    tabla.field_names = ["Código", "Nombre", "Descripción", "Creditos", "Docente"]
    for curso in cursos:
        tabla.add_row([curso[0], curso[1], curso[2], curso[3], f"{curso[4]} {curso[5]}"])
    print(tabla)

def mostrar_curso_por_docente(cursos):
    """Muestra la información de un curso por el id del docente."""
    tabla = PrettyTable()

    tabla.field_names = ["Nombre", "Descripción", "Creditos"]
    for curso in cursos:
        tabla.title = f"Cursos dictados por el docente {curso[3]} {curso[4]}"
        tabla.add_row([curso[0], curso[1], curso[2]])
    print(tabla)