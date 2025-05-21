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
INSERT INTO estudiantes (numero_documento, nombre, apellido, fecha_nacimiento, email, telefono) 
VALUES ('1234567890', 'Juan', 'Pérez', '1990-01-15', 'l@example.com', '1234567890');

-- Consulta de cursos con nombre de docente
SELECT c.id_curso, c.nombre_curso, c.descripcion, c.creditos, d.nombre AS nombre_docenente, d.apellido as apellido_docente  
FROM cursos c
JOIN docentes d ON c.id_docente = d.id_docente;

-- consulta de cursos que dicta un docente
SELECT c.nombre_curso, c.descripcion, c.creditos, d.nombre, d.apellido  
FROM cursos c
JOIN docentes d ON c.id_docente = d.id_docente
WHERE d.numero_documento = '456789123';

-- Consulta de los estudiantes inscritos en un curso
SELECT i.id_inscripcion, e.numero_documento, e.nombre, e.apellido, c.id_curso, c.nombre_curso, i.fecha_inscripcion
FROM inscripciones i
JOIN estudiantes e ON i.id_estudiante = e.id_estudiante
JOIN cursos c ON i.id_curso = c.id_curso;

-- Consulta de los estudiantes inscritos en un curso
SELECT i.id_inscripcion, e.numero_documento, e.nombre, e.apellido, c.id_curso, c.nombre_curso, i.fecha_inscripcion
FROM inscripciones i
JOIN estudiantes e ON i.id_estudiante = e.id_estudiante
JOIN cursos c ON i.id_curso = c.id_curso
WHERE e.numero_documento = '1234567890';