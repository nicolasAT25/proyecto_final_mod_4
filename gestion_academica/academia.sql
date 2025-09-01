-- Crear la base de datos
CREATE DATABASE academia;

-- Crear la tabla de estudiantes
CREATE TABLE IF NOT EXISTS estudiantes (
    id_estudiante BIGSERIAL PRIMARY KEY,
    numero_documento VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(20) NOT NULL
);

-- Crear la tabla de docentes
CREATE TABLE IF NOT EXISTS docentes (
    id_docente BIGSERIAL PRIMARY KEY,
    numero_documento VARCHAR(20) NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    apellido VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    telefono VARCHAR(20) NOT NULL,
    especialidad VARCHAR(100) NOT NULL
);

-- Crear la tabla de cursos
CREATE TABLE IF NOT EXISTS cursos (
    id_curso BIGSERIAL PRIMARY KEY,
    nombre_curso VARCHAR(255) NOT NULL,
    descripcion TEXT NOT NULL,
    creditos INT NOT NULL,
    id_docente BIGINT NOT NULL,
    FOREIGN KEY (id_docente) REFERENCES docentes(id_docente)
);

-- Crear la tabla de inscripciones
CREATE TABLE IF NOT EXISTS inscripciones (
    id_inscripcion BIGSERIAL PRIMARY KEY,
    id_estudiante BIGINT NOT NULL,
    id_curso BIGINT NOT NULL,
    fecha_inscripcion DATE NOT NULL,
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante),
    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso)
);