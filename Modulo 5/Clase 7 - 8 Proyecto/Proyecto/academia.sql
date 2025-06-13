-------------------------------------------------
-- Script para crear la base de datos y las tablas del proyecto Academia Python C2
CREATE DATABASE academiaPythonC2;

------------------------------------------------
-- Tabla: Programas
-- Almacenar los programa academicos disponibles
CREATE TABLE IF NOT EXISTS programas (
    id SERIAL PRIMARY KEY,
    nombre_programa VARCHAR(100) NOT NULL
)

-----------------------------------------------

-- Tabla: Alumnos
-- Almacenar la información de los alumnos
CREATE TABLE IF NOT EXISTS alumnos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    programa_id INT NOT NULL,
    FOREIGN KEY (programa_id) REFERENCES programas(id)
);

------------------------------------------------
-- Tabla: Notas
-- Almacenar las notas de los alumnos
CREATE TABLE IF NOT EXISTS notas (
    id SERIAL PRIMARY KEY,
    alumno_id INT NOT NULL,
    materia VARCHAR(100) NOT NULL,
    nota DECIMAL(5, 2) CHECK (nota >= 0 AND nota <= 100),
    FOREIGN KEY (alumno_id) REFERENCES alumnos(id)
);

------------------------------------------------