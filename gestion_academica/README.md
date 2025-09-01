# PROYECTO GESTIÓN ACADÉMICA 👩🏻‍🎓👨🏽‍🎓

## 1. Nuevas Funcionalidades/Mejoras ⚙️

### 1.1. Mejoras

* Se migra la DB de `MySQL` a `PostgreSQL`.
* Uso de archivo `.env` para las credenciales a la DB.
* Se añade archivo `.gitignore` para gestionar _push_ de los archivos al repositorio.
* Los archivos `__init__.py` son agregados a los directorios que se requieren importar como módulos de Python.
* `Snake Case` para el nombre de archivos y funciones.
* Corrección de _typos_.
* Uso del idioma inglés para archivos, variables y funciones para mayor consistencia.

### 1.2. Nuevas Funcionealidades

* 


## 2. Tech Stack

* `Python==3.12.3`
* `PostgreSQL==17.5 (Homebrew)`
* `pgAdmin==9.4`

## 3. Bibliotecas / Libraries

* `prettytable`
* `psycopg`

### 3.1. Instalación

```bash
pip install "psycopg[binary]"
pip install prettytable