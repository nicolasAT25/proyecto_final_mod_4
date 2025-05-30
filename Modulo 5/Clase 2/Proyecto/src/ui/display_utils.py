from typing import List, Dict, Any

def print_success(message: str) -> None:
    print(f"\033[32m{message}\033[0m")

def print_error(message: str) -> None:
    print(f"\033[31m{message}\033[0m")

def print_info(message: str) -> None:
    print(f"\033[34m{message}\033[0m")

def print_warning(message: str) -> None:
    print(f"\033[33m{message}\033[0m")

def print_table(rows, headers,title=None): 
    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = headers
    table.title = title
    for row in rows:
        # limitar la cantidad de caracteres en las columnas
        table.add_row([str(getattr(row, col))[:50] + "..." if len(str(getattr(row, col))) > 50 else str(getattr(row, col)) for col in headers])

        #table.add_row([str(getattr(row, col)) for col in headers])
    print(table)

def print_table_medicamentos(rows, headers,title=None): 
    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = headers
    table.title = title
    

    for row in rows:
        display_row = []
        for header in headers:
            if header == 'id':
                display_row.append(row.id)
            elif header == 'ubicacion':
                display_row.append(row.ubicacion.nombre if row.ubicacion else 'N/A')
            elif header == 'medicamento':
                display_row.append(row.medicamento.nombre if row.medicamento else 'N/A')
            elif header == 'cantidad':
                display_row.append(row.cantidad)
            else:
                display_row.append(getattr(row, header, 'N/A'))

        table.add_row(display_row) 
    print(table)
