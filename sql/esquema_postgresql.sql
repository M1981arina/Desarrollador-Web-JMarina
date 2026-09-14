CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    rol VARCHAR(50) NOT NULL DEFAULT 'Usuario'
);

CREATE TABLE IF NOT EXISTS obras (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    descripcion VARCHAR(500) NOT NULL,
    ubicacion VARCHAR(150),
    presupuesto NUMERIC(12, 2),
    estado VARCHAR(30) NOT NULL DEFAULT 'Registrada',
    responsable_id INTEGER REFERENCES usuarios(id)
        ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS tramites_solicitudes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    tipo VARCHAR(80) NOT NULL,
    detalle VARCHAR(500) NOT NULL,
    estado VARCHAR(30) NOT NULL DEFAULT 'Recibida'
);
