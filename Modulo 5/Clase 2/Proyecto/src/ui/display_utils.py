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
        table.add_row([str(getattr(row, col)) for col in headers])
    print(table)