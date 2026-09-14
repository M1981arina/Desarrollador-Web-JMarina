CREATE DATABASE IF NOT EXISTS arenillas;
USE arenillas;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    rol VARCHAR(50) NOT NULL DEFAULT 'Usuario'
);

CREATE TABLE IF NOT EXISTS obras (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    descripcion VARCHAR(500) NOT NULL,
    ubicacion VARCHAR(150),
    presupuesto DECIMAL(12, 2),
    estado VARCHAR(30) NOT NULL DEFAULT 'Registrada',
    responsable_id INT NULL,
    CONSTRAINT fk_obra_responsable
        FOREIGN KEY (responsable_id) REFERENCES usuarios(id)
        ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS tramites_solicitudes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    tipo VARCHAR(80) NOT NULL,
    detalle VARCHAR(500) NOT NULL,
    estado VARCHAR(30) NOT NULL DEFAULT 'Recibida'
);
