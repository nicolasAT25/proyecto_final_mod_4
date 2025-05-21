from controller import inscripcionesController

def menuIncripciones():
    while True:
        print("\n--- Menú de Inscripciones ---")
        print("1. Ver Inscripciones")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inscripcionesController.mostrar_inscripciones()
        elif opcion == "2":
            print("Saliendo del menú de inscripciones.")
            break
        else:
            print("Opción no válida. Intente de nuevo.") 