from controller import courses_controller

def courses_menu():
    while True:
        print("\n--- Menú de Cursos ---")
        print("1. Crear Curso")
        print("2. Ver Cursos")
        print("3. Ver Cursos por ID Docente")
        print("4. Ver Cursos por ID Curso")
        print("5. Actualizar Curso por ID")
        print("6. Eliminar Curso por ID")
        print("7. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            nombre_curso = input("Ingrese el nombre del curso: ")
            descripcion = input("Ingrese la descripción del curso: ")
            creditos = input("Ingrese los créditos del curso: ")
            id_docente = input("Ingrese el ID del docente: ")
            
            courses_controller.create_course(nombre_curso, descripcion, creditos, id_docente)
        elif opcion == "2":
            courses_controller.show_courses()
        elif opcion == "3":
            id_docente = input("Ingrese el ID del docente: ")
            courses_controller.show_course_by_teacher_id(id_docente)
        elif opcion == "4":
            id_curso = input("Ingrese el ID del curso: ")
            courses_controller.show_course_by_course_id(id_curso)
        elif opcion == "5":
            id_curso = input("Ingrese el ID del curso a modificar: ")
            courses_controller.update_course(id_curso)
        elif opcion == "6":
            id_curso = input("Ingrese el ID del curso a eliminar: ")
            courses_controller.delete_course(id_curso)
        elif opcion == "7":
            print("Saliendo del menú de cursos.")
            break
        else:
            print("Opción no válida. Intente de nuevo.") 