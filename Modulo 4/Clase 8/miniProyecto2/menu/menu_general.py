from menu.menu_estudiantes import menuEstudiantes
from menu.menu_docentes import menuDocente
from menu.menu_cursos import menuCursos
from menu.menu_inscripciones import menuIncripciones

def menuGeneral():
    while True:
        print("\n--- Menú General ---")
        print("1. Menú de Estudiantes")
        print("2. Menú de Docentes")
        print("3. Menú de Cursos")
        print("4. Menú de Inscripciones")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menuEstudiantes()
        elif opcion == "2":
            menuDocente()
        elif opcion == "3":
            menuCursos()
        elif opcion == "4":
            menuIncripciones()
        elif opcion == "5":
            print("Saliendo del menú general.")
            break
        else:
            print("Opción no válida. Intente de nuevo.") 