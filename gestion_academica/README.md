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
* Se modifican las actualizaciones en los modelos de tal manera que se verifica la existencia del registro y luego sí se solicitan los nuevos valores (si es que se quieren modificar).

### 1.2. Nuevas Funcionealidades

* Se añaden el resto de operaciones CRUD a los modelos de `cursos` e `inscripciones` así como sus respectivas vistas, controladores y menús.


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
```

## 4. Esquema de la base de datos

Ejecutar el el script de SQL `academia.sql`, esto creará la DB `academia` y las tablas `estudiantes`, `docentes`, `cursos` e `inscripciones`.