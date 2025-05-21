from models import cursosModel
from views import cursosView

def mostrar_cursos():
    """Mostrar la lista de cursos."""
    cursos = cursosModel.consultarCursos()
    if cursos:
        cursosView.mostrar_cursos(cursos)
    else:
        print("No hay cursos registrados.")

def mostrar_curso_por_docente(id_docente):
    """Mostrar los cursos dictados por un docente específico."""
    cursos = cursosModel.consultarCursoPorDocente(id_docente)
    if cursos:
        cursosView.mostrar_curso_por_docente(cursos)
    else:
        print("No hay cursos registrados para este docente.")
