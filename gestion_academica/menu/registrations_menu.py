from controller import registrations_controller

def registrations_menu():
    while True:
        print("\n--- Menú de Inscripciones ---")
        print("1. Crear Inscripción")
        print("2. Ver Inscripciones")
        print("3. Ver Inscripción por ID")
        print("4. Modificar Inscripción por ID")
        print("5. Eliminar Inscripción por ID")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_estudiante = input("Ingrese el ID del estudiante: ")
            id_curso = input("Ingrese el ID del curso: ")
            fecha_inscripcion = input("Ingrese la fecha de inscripción (YYYY-MM-DD): ")
            registrations_controller.create_course(id_estudiante, id_curso, fecha_inscripcion)
        elif opcion == "2":
            registrations_controller.show_registrations()
        elif opcion == "3":
            id_inscripcion = input("Ingrese el ID de la inscripción: ")
            registrations_controller.show_registration(id_inscripcion)
        elif opcion == "4":
            id_inscripcion = input("Ingrese el ID de la inscripción a modificar: ")
            registrations_controller.update_registration(id_inscripcion)
        elif opcion == "5":
            id_inscripcion = input("Ingrese el ID de la inscripción a eliminar: ")
            registrations_controller.delete_registration(id_inscripcion)
        elif opcion == "6":
            print("Saliendo del menú de inscripciones.")
            break
        else:
            print("Opción no válida. Intente de nuevo.") 