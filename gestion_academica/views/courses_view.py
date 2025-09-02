from prettytable import PrettyTable

def show_courses(courses):
    """Muestra la información de un curso."""
    table = PrettyTable()
    table.title = "Cursos"
    table.field_names = ["Código", "Nombre", "Descripción", "Creditos", "Docente"]
    for course in courses:
        table.add_row([course["id_curso"], course["nombre_curso"], course["descripcion"], course["creditos"], f"{course["nombre_docente"]} {course["apellido_docente"]}"])
    print(table)

def show_course_by_teacher_id(courses):
    """Muestra la información de un curso por el id del docente."""
    table = PrettyTable()
    table.field_names = ["Nombre", "Descripción", "Creditos"]
    for course in courses:
        table.title = f"Cursos dictados por el docente {course["nombre_docente"]} {course["apellido_docente"]}"
        table.add_row([course["nombre_curso"], course["descripcion"], course["creditos"]])
    print(table)

def show_course_by_course_id(course):
    """Muestra la información de un curso por el id del docente."""
    table = PrettyTable()
    table.field_names = ["Nombre", "Descripción", "Creditos"]
    table.add_row([course[0]["nombre_curso"], course[0]["descripcion"], course[0]["creditos"]])
    print(table)