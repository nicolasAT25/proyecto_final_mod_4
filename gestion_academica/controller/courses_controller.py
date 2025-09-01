from models import courses_model
from views import courses_view

def mostrar_cursos():
    """Mostrar la lista de cursos."""
    cursos = courses_model.read_courses()
    if cursos:
        courses_view.mostrar_cursos(cursos)
    else:
        print("No hay cursos registrados.")

def mostrar_curso_por_docente(id_docente):
    """Mostrar los cursos dictados por un docente específico."""
    cursos = courses_model.read_course_by_teacher_id(id_docente)
    if cursos:
        courses_view.mostrar_curso_por_docente(cursos)
    else:
        print("No hay cursos registrados para este docente.")