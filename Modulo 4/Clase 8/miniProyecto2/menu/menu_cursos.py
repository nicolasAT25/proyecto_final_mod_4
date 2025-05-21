from controller import cursosController

def menuCursos():
    while True:
        print("\n--- Menú de Cursos ---")
        print("1. Ver Cursos")
        print("2. Ver Cursos por Docente")
        print("6. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            cursosController.mostrar_cursos()
        elif opcion == "2":
            id_docente = input("Ingrese el número de documento del docente: ")
            cursosController.mostrar_curso_por_docente(id_docente)
        elif opcion == "6":
            print("Saliendo del menú de cursos.")
            break
        else:
            print("Opción no válida. Intente de nuevo.") 