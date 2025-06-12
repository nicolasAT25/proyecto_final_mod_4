import sys
from enum import Enum
import os

def get_string_input(prompt: str, required: bool = True) -> str | None:
    while True:
        user_input = input(prompt)
        if not user_input and required:
            print("Este campo es requerido. Por favor, ingresa un valor.")
            continue
        return user_input if user_input else None
    
def get_init_input(prompt: str, min_value: int = 0, max_value: int = sys.maxsize, required: bool = True) -> int | None:
    while True:
        value_str = input(prompt).strip()
        if not value_str and not required:
            return None
        if not value_str and required:
            print("Este campo es requerido. Por favor, ingresa un valor.")
            continue
        try:
            value = int(value_str)
            if value < min_value:
                print(f"El valor debe ser mayor o igual a {min_value}. Por favor, ingresa un valor valido.")
                continue
            return value
        except ValueError:
            print("Por favor, ingresa un valor valido.")

def verificador_exitencia():
    pass

def clear_screen():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")