from models import courses_model
from views import courses_view

def create_course(nombre_curso, descripcion, creditos, id_docente):
    """Crear un nuevo curso."""
    courses_model.create_course(nombre_curso, descripcion, creditos, id_docente)
    print("Curso creado exitosamente.")

def show_courses():
    """Mostrar la lista de cursos."""
    cursos = courses_model.read_courses()
    if cursos:
        courses_view.show_courses(cursos)
    else:
        print("No hay cursos registrados.")

def show_course_by_teacher_id(id_docente):
    """Mostrar los cursos dictados por un docente específico."""
    cursos = courses_model.read_course_by_teacher_id(id_docente)
    if cursos:
        courses_view.show_course_by_teacher_id(cursos)
    else:
        print("No hay cursos registrados para este docente.")

def show_course_by_course_id(id_curso):
    """Mostrar un curso por su ID."""
    curso = courses_model.read_course_by_teacher_id(id_curso)
    if curso:
        courses_view.show_course_by_course_id(curso)
    else:
        print("No hay cursos registrados para este ID.")
        
def update_course(id_curso):
    """Modificar un estudiante existente."""
    courses_model.update_course_by_id(id_curso)
    print("Curso modificado exitosamente.")
    
def delete_course(id_curso):
    """Eliminar un estudiante por número de documento."""
    courses_model.delete_course(id_curso)
    print("Curso eliminado exitosamente.")