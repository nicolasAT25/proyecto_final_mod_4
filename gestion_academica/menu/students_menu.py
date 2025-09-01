from gestion_academica.controller import students_controller

def students_menu():
    while True:
        print("\n--- Menú de Estudiantes ---")
        print("1. Crear Estudiante")
        print("2. Mostrar Estudiantes")
        print("3. Buscar Estudiante por Documento")
        print("4. Modificar Estudiante")
        print("5. Eliminar Estudiante")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero_documento = input("Ingrese el número de documento: ")
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
            email = input("Ingrese el email: ")
            telefono = input("Ingrese el teléfono: ")

            students_controller.crear_estudiante(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
        elif opcion == "2":
            students_controller.mostar_estudiantes() 
        elif opcion == "3":
            id_estudiante = input("Ingrese el número de documento del estudiante: ")
            students_controller.mostrar_estudiante(id_estudiante)
        elif opcion == "4":
            numero_documento = input("Ingrese el número de documento del estudiante a modificar: ")
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento (YYYY-MM-DD): ")
            email = input("Ingrese el nuevo email: ")
            telefono = input("Ingrese el nuevo teléfono: ")

            students_controller.modificar_estudiante(numero_documento, nombre, apellido, fecha_nacimiento, email, telefono)
        elif opcion == "5":
            numero_documento = input("Ingrese el número de documento del estudiante a eliminar: ")
            students_controller.eliminar_estudiante(numero_documento)
        elif opcion == "6":
            print("Saliendo del menú de estudiantes.")
            break
        else:
            print("Opción no válida. Intente de nuevo.") 