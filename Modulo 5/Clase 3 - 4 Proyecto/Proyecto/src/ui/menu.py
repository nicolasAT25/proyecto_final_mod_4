import sys
from sqlalchemy.orm import Session
from database.connections import get_db
from services import inventory_service, dispatch_service, report_service
from ui.input_utils import get_init_input, get_string_input,get_init_input, clear_screen
from ui.display_utils import print_success, print_info, print_error, print_warning, print_table, print_table_medicamentos
from models.ticket_despacho_bodega import EstadoTicketDespacho
from models.ubicacion import TipoUbicacion

def _display_invenroty_management_menu():
    clear_screen()
    print("Gestion de Inventarios")
    print("1. Gestionar Medicamentos")
    print("2. Gestionar Ubicaciones")
    print("3. Gestionar Stock")
    print("4. Volver al Menu Principal")
    return get_string_input("Seleccione una opcion: ", required=True)

def handle_inventory_menu():
    while True:
        choise = _display_invenroty_management_menu()
        if choise == "1":
            _handle_medicamento_menu()
        elif choise == "2":
            _handle_ubicacion_menu()
        elif choise == "3":
            _handle_stock_menu()
        elif choise == "4":
            break
        else:
            print_warning("Opcion no valida")
        input("Presiona enter para continuar...")

def _handle_stock_menu():
    while True:
        clear_screen()
        print("Gestion de Stock")
        print("1. ver todo el stock")
        print("2. agregar stock / actualizar stock")
        print("3. eliminar stock")
        print("4. Volver al Menu Principal")


        choise = get_string_input("Seleccione una opcion: ", required=True)

        with get_db() as db:
            if choise == "1":
                ver_inventario()
                input("Presiona enter para continuar...")

            elif choise == "2":
                clear_screen()
                ver_ubicaciones()
                ver_medicamentos()
                ver_inventario()
                
                medicamento_id = get_init_input("Ingrese el id del medicamento: ", min_value=1, required=True) 
                ubicacion_id = get_init_input("Ingrese el id de la ubicacion: ", min_value=1, required=True) 
                cantidad = get_init_input("Ingrese la cantidad de medicamentos: ", min_value=1, required=True)

                isvu = inventory_service.verificador_de_ubicacion_dentro_de_inventario(db, ubicacion_id)
                isvm = inventory_service.verificardor_de_medidicamento_dentro_de_inventario(db, medicamento_id)

                if isvu and isvm:
                    print_info("Este medicamento ya se encuentra en esta ubicacion")
                    print_info("Deseas actualizar el stock?")
                    print("1. Si")
                    print("2. No")
                    respuesta = get_init_input("Seleccione una opcion: ", min_value=1, max_value=2, required=True)
                    
                    if respuesta == 1:
                        if inventory_service.update_stock(db, isvm.id, ubicacion_id, medicamento_id, cantidad):
                            print_success("Stock actualizado correctamente")
                        else:
                            print_error("No se pudo actualizar el stock")
                    else:
                        print_info("Stock no actualizado")

                else:
                    if inventory_service.add_inventario(db, medicamento_id, ubicacion_id, cantidad):
                        print_success("Stock agregado correctamente")
                    else:
                        print_error("No se pudo agregar el stock")

                input("Presiona enter para continuar...")
                
            elif choise == "3":
                ver_inventario()
                inventario_id = get_init_input("Ingrese el id de la ubicacion: ", min_value=1, required=True)

                if inventory_service.delete_inventario(db, inventario_id):
                    print_success("Ubicacion eliminada correctamente")
                else:
                    print_error("No se pudo eliminar la ubicacion")

                input("Presiona enter para continuar...")

            elif choise == "4":
                break
                

def ver_inventario():
    with get_db() as db:
        if stock := inventory_service.get_inventario_all(db):
            headers = ["id", "ubicacion", "medicamento", "cantidad"]
            print_info("Stock")
            print_table_medicamentos(stock, headers, title="Stock")
        else:
            print_warning("No hay stock disponible")

def _handle_ubicacion_menu():
    while True:
        clear_screen()
        print("Gestion de Ubicaciones")
        print("1. Agregar Ubicacion")
        print("2. Ver todas las Ubicaciones")
        print("3. Actualizar Ubicacion")
        print("4. Volver al Menu Principal")
        choise = get_string_input("Seleccione una opcion: ", required=True)

        with get_db() as db:
            if choise == "1":
                nombre = get_string_input("Ingrese el nombre de la ubicacion: ", required=True)
                print ("Seleccione el tipo de ubicacion:")
                print("1. Bodega")
                print("2. Local")
                tipo = get_init_input("Seleccione una opcion: ", min_value=1, max_value=2, required=True)

                if tipo == 1:
                    ubicacion = inventory_service.add_ubicacion(db, nombre, TipoUbicacion.BODEGA)
                elif tipo == 2:
                    ubicacion = inventory_service.add_ubicacion(db, nombre, TipoUbicacion.LOCAL)

                if ubicacion:
                    print_success(f"Ubicacion {ubicacion.nombre} agregada correctamente")
                else:
                    print_error("Error al agregar la ubicacion")
                
                input("Presiona enter para continuar...")

            elif choise == "2":
                ver_ubicaciones()
            elif choise == "3":
                
                id_ubicacion = get_init_input("Ingrese el id de la ubicacion: ", min_value=1, required=True)
                ubicacion = inventory_service.get_ubicacion_by_id(db, int(id_ubicacion))
                if ubicacion:
                    nombre = get_string_input("Ingrese el nombre de la ubicacion: ", required=True)
                    print ("Seleccione el tipo de ubicacion:")
                    print("1. Bodega")
                    print("2. Local")
                    tipo = get_init_input("Seleccione una opcion: ", min_value=1, max_value=2, required=True)

                    if tipo == 1:
                        ubicacion = inventory_service.update_ubicacion(db, int(id_ubicacion), {"nombre": nombre, "tipo": TipoUbicacion.BODEGA})
                    elif tipo == 2:
                        ubicacion = inventory_service.update_ubicacion(db, int(id_ubicacion), {"nombre": nombre, "tipo": TipoUbicacion.LOCAL})
                    
                    if ubicacion:
                        print_success(f"Ubicacion {ubicacion.nombre} actualizada correctamente")
                    else:
                        print_error("Error al actualizar la ubicacion")
            elif choise == "4":
                break

def ver_ubicaciones():
    with get_db() as db:
        ubicaciones = inventory_service.get_all_ubicaciones(db)
        if ubicaciones:
            headers = ["id", "nombre", "tipo"]
            titulo = "Ubicaciones"
            print_table(ubicaciones, headers, titulo)
        else:
            print_warning("No se encontraron ubicaciones")

def _handle_medicamento_menu():
    while True:
        clear_screen()
        print("Gestion de Medicamentos")
        print("1. Agregar Medicamento")
        print("2. Ver todos los Medicamentos")
        print("3. Actualizar Medicamento")
        print("4. Elminar Medicamento")
        print("5. Volver al Menu Principal")
        choise = get_string_input("Seleccione una opcion: ", required=True)

        with get_db() as db:
            if choise == "1":
                nombre = get_string_input("Ingrese el nombre del medicamento: ", required=True)
                descripcion = get_string_input("Ingrese la descripcion del medicamento: ", required=True)
                codigo_barras = get_string_input("Ingrese el codigo de barras del medicamento: ", required=True)

                med = inventory_service.add_medicamento(db, nombre, descripcion, codigo_barras)

                if med:
                    print_success(f"Medicamento {med.nombre} agregado correctamente")
                else:
                    print_error("Error al agregar el medicamento")
                
                input("Presiona enter para continuar...")

            elif choise == "2":
                ver_medicamentos()
                input("Presiona enter para continuar...")
            elif choise == "3":
                selected_id = get_init_input("Ingrese el id del medicamento a actualizar: ", required=True)

                if medicamento := inventory_service.get_medicamento_by_id(db, selected_id):
                    nombre = get_string_input("Ingrese el nuevo nombre del medicamento: ", required=True)
                    descripcion = get_string_input("Ingrese la nueva descripcion del medicamento: ", required=True)
                    codigo_barras = get_string_input("Ingrese el nuevo codigo de barras del medicamento: ", required=True)

                    dict_medicamento = {

                        "nombre": nombre,
                        "descripcion": descripcion,
                        "codigo_barras": codigo_barras
                    }

                    med = inventory_service.update_medicamento(db, selected_id ,dict_medicamento)

                    if med:
                        print_success(f"Medicamento {med.nombre} actualizado correctamente")
                    else:
                        print_error("Error al actualizar el medicamento")
                    
                    input("Presiona enter para continuar...")
                else:
                    print_error("Medicamento no encontrado")
                    input("Presiona enter para continuar...")
            elif choise == "4":
                selected_id = get_init_input("Ingrese el id del medicamento a eliminar: ", required=True)


                if inventory_service.delete_medicamento(db, selected_id):
                    print_success(f"Medicamento eliminado correctamente")
                else:
                    print_error("Error al eliminar el medicamento")
                
                input("Presiona enter para continuar...")
            elif choise == "5":
                break

def ver_medicamentos():
    with get_db() as db:
        medicamentos = inventory_service.get_all_medicamentos(db)
        if medicamentos:
            headers = ["id", "nombre", "descripcion", "codigo_barras"]
            titulo = "Medicamentos"
            print_table(medicamentos, headers, titulo)
        else:
            print_warning("No se encontraron medicamentos")

def display_main_menu():
    clear_screen()
    print("Menu Principal")
    print("1. Gestion de Inventarios / Medicamentos")
    print("2. Gestion de Tickets Despacho Bodega / despachos")
    print("3. Informes")
    print("0. Salir")
    return get_string_input("Seleccione una opcion: ", required=True)

def handle_main_menu():
    while True:
        choise = display_main_menu()
        if choise == "1":
            handle_inventory_menu()
        elif choise == "2":
            pass
        elif choise == "3":
            pass
        elif choise == "0":
            break
        else:
            print_warning("Opcion no valida")
        input("Presiona enter para continuar...")

