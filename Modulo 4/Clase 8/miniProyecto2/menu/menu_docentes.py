from controller import docentesController

def menuDocente():
    while True:
        print("\n--- Menú de Docentes ---")
        print("1. Crear Docente")
        print("2. Mostrar Docentes")
        print("3. Buscar Docente por Documento")
        print("4. Actualizar Docente")
        print("5. Eliminar Docente")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero_documento = input("Ingrese el número de documento: ")
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            email = input("Ingrese el email: ")
            telefono = input("Ingrese el teléfono: ")
            especialidad = input("Ingrese la especialidad: ")

            docentesController.crear_docente(numero_documento, nombre, apellido, email, telefono, especialidad)
        elif opcion == "2":
            docentesController.mostrar_docentes()
        elif opcion == "3":
            numero_documento = input("Ingrese el número de documento del docente: ")
            docentesController.mostrar_docente(numero_documento)
        elif opcion == "4":
            numero_documento = input("Ingrese el número de documento del docente a actualizar: ")
            nombre = input("Ingrese el nuevo nombre: ")
            apellido = input("Ingrese el nuevo apellido: ")
            email = input("Ingrese el nuevo email: ")
            telefono = input("Ingrese el nuevo teléfono: ")
            especialidad = input("Ingrese la nueva especialidad: ")

            docentesController.modificar_docente(numero_documento, nombre, apellido, email, telefono, especialidad)
        elif opcion == "5":
            numero_documento = input("Ingrese el número de documento del docente a eliminar: ")
            docentesController.eliminar_docente(numero_documento)
        elif opcion == "6":
            print("Saliendo del menú de docentes.")
            break
        else:
            print("Opción no válida. Intente de nuevo.") 