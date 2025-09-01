from menu.students_menu import students_menu
from menu.teachers_menu import teachers_menu
from menu.courses_menu import courses_menu
from menu.registrations_menu import registrations_menu

def main_menu():
    while True:
        print("\n--- Menú General ---")
        print("1. Menú de Estudiantes")
        print("2. Menú de Docentes")
        print("3. Menú de Cursos")
        print("4. Menú de Inscripciones")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            students_menu()
        elif opcion == "2":
            teachers_menu()
        elif opcion == "3":
            courses_menu()
        elif opcion == "4":
            registrations_menu()
        elif opcion == "5":
            print("Saliendo del menú general.")
            break
        else:
            print("Opción no válida. Intente de nuevo.") 