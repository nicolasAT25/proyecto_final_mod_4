-- Crear nuestra base de datos
CREATE DATABASE IF NOT EXISTS academia;

-- Usar la base de datos
USE academia;

-- Crear la tabla de estudiantes
CREATE TABLE IF NOT EXISTS estudiantes (
    id_estudiante bigint AUTO_INCREMENT PRIMARY KEY,
    numero_documento VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(20) NOT NULL
);

-- Crear la talba de docentes
CREATE TABLE IF NOT EXISTS docentes (
    id_docente bigint AUTO_INCREMENT PRIMARY KEY,
    numero_documento VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(20) NOT NULL,
    especialidad VARCHAR(100) NOT NULL
);

-- Crear la tabla de cursos
CREATE TABLE IF NOT EXISTS cursos (
    id_curso bigint AUTO_INCREMENT PRIMARY KEY,
    nombre_curso VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    creditos INT NOT NULL,
    id_docente bigint NOT NULL,
    FOREIGN KEY (id_docente) REFERENCES docentes(id_docente)
);

-- Crear la tabla de inscripciones
CREATE TABLE IF NOT EXISTS inscripciones (
    id_inscripcion bigint AUTO_INCREMENT PRIMARY KEY,
    id_estudiante bigint NOT NULL,
    id_curso bigint NOT NULL,
    fecha_inscripcion DATE NOT NULL,
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante),
    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
);

-- Insertar datos en la tabla de estudiantes
INSERT INTO estudiantes (nombre, apellido, fecha_nacimiento, email, telefono) 
VALUES ('Juan', 'Pérez', '1990-01-15', 'l@example.com', '1234567890');

-- Insertar multiples datos en la tabla de estudiantes
INSERT INTO estudiantes (nombre, apellido, fecha_nacimiento, email, telefono) 
VALUES ('Pedro', 'Gómez', '1995-05-20', 'sKZjC@example.com', '9876543210'),
       ('María', 'López', '1992-03-10', 'o@example.com', '5555555555'),
       ('Ana', 'García', '1998-01-05', 'a@example.com', '6666666666'),
       ('Tomás', 'González', '1991-12-25', 't@example.com', '7777777777'),
       ('Luis', 'Rodríguez', '1996-06-15', 'x@example.com', '8888888888');

-- Insertar datos en la tabla de docentes
INSERT INTO docentes (nombre, apellido, email, telefono, especialidad)
VALUES 
        ('Andrés', 'Sánchez', 'andres.sanchez@example.com', '1111111111', 'Matemáticas'),
       ('Sofía', 'González', 'sofia.gonzalez@example.com', '2222222222', 'Física'),
       ('Cristina', 'López', 'cristina.lopez@example.com', '3333333333', 'Química'),
       ('Miguel', 'García', 'miguel.garcia@example.com', '4444444444', 'Biología'),
       ('Marcela', 'Rodríguez', 'marcela.rodriguez@example.com', '5555555555', 'Computación');

-- Insertar datos en la tabla de cursos
INSERT INTO cursos (nombre_curso, descripcion, creditos, id_docente)
VALUES ('Matemáticas avanzadas', 'Aprender matemáticas avanzadas', 5, 1),
       ('Física avanzada', 'Aprender fisica avanzada', 4, 2),
       ('Química avanzada', 'Aprender química avanzada', 3, 3),
       ('Biología avanzada', 'Aprender biología avanzada', 4, 4),
       ('Computación avanzada', 'Aprender computación avanzada', 5, 5);
       
-- Insertar datos en la tabla de inscripciones
INSERT INTO inscripciones (id_estudiante, id_curso, fecha_inscripcion)
VALUES (1, 1, '2023-01-01'),
       (8, 2, '2023-02-01'),
       (9, 3, '2023-03-01'),
       (10, 4, '2023-04-01'),
       (11, 5, '2023-05-01');

-- Consultas todos los estudiantes
SELECT * FROM estudiantes;

-- Consultar todos los docentes
SELECT * FROM docentes;

-- Consultar todos los cursos
SELECT * FROM cursos;

-- Consultar todos los inscriptos
SELECT * FROM inscripciones;

-- Consultas con datos especificos
SELECT nombre, apellido, email, telefono FROM estudiantes;

-- Consultas con filtros
SELECT * FROM estudiantes WHERE fecha_nacimiento > '1995-01-01';
SELECT * FROM estudiantes WHERE nombre LIKE 'M%';
SELECT * FROM estudiantes WHERE email = 'l@example.com';

-- Consultas con ordenamiento
SELECT * FROM estudiantes ORDER BY fecha_nacimiento DESC;
SELECT * FROM estudiantes ORDER BY nombre ASC;
SELECT * FROM estudiantes ORDER BY nombre DESC;

-- Consulta con filtros y ordenamiento
SELECT * FROM estudiantes WHERE fecha_nacimiento > '1995-01-01' 
ORDER BY nombre ASC;

-- Consultas con joins
SELECT e.nombre, e.apellido, c.nombre_curso
FROM estudiantes e
JOIN inscripciones i ON e.id_estudiante = i.id_estudiante
JOIN cursos c ON i.id_curso = c.id_curso;

-- Consultar los cursos y sus docentes ordenados por nombre de curso
SELECT c.nombre_curso, d.nombre as 'nombre_docente', d.apellido as 'apellido_docente'
FROM cursos c
JOIN docentes d ON c.id_docente = d.id_docente
ORDER BY c.nombre_curso ASC;

