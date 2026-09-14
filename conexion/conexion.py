import os
import sqlite3

try:
    import mysql.connector
except ImportError:
    mysql = None

from db import obtener_conexion

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DATABASE_PATH = os.path.join(DATA_DIR, "ferreteria.db")
USING_MYSQL = os.getenv("MYSQL_HOST") is not None
USING_POSTGRES = os.getenv("POSTGRES_HOST") is not None
MYSQL_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "port": int(os.getenv("MYSQL_PORT", "3306")),
    "database": os.getenv("MYSQL_DATABASE", "arenillas"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
}


def get_db_connection():
    if USING_POSTGRES:
        connection = obtener_conexion()
        if connection is None:
            raise RuntimeError("No se pudo conectar con PostgreSQL. Revisa las variables POSTGRES_*. ")
        return connection

    if USING_MYSQL:
        if mysql is None:
            raise RuntimeError("Instala mysql-connector-python para utilizar MySQL.")
        return mysql.connector.connect(**MYSQL_CONFIG)

    os.makedirs(DATA_DIR, exist_ok=True)
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def execute_db(conn, query, params=()):
    if USING_POSTGRES:
        from psycopg2.extras import RealDictCursor

        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute(query.replace("?", "%s"), params)
        return cursor

    if USING_MYSQL:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(query.replace("?", "%s"), params)
        return cursor
    return conn.execute(query, params)


def init_db():
    conn = get_db_connection()
    try:
        if USING_POSTGRES:
            id_definition = "SERIAL PRIMARY KEY"
        elif USING_MYSQL:
            id_definition = "INT PRIMARY KEY AUTO_INCREMENT"
        else:
            id_definition = "INTEGER PRIMARY KEY AUTOINCREMENT"
        execute_db(
            conn,
            f"""
            CREATE TABLE IF NOT EXISTS usuarios (
                id {id_definition},
                nombre VARCHAR(100) NOT NULL,
                email VARCHAR(150) NOT NULL UNIQUE,
                rol VARCHAR(50) NOT NULL DEFAULT 'Usuario'
            )
            """,
        )
        execute_db(
            conn,
            f"""
            CREATE TABLE IF NOT EXISTS obras (
                id {id_definition},
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
            )
            """,
        )
        execute_db(
            conn,
            f"""
            CREATE TABLE IF NOT EXISTS tramites_solicitudes (
                id {id_definition},
                nombre VARCHAR(100) NOT NULL,
                email VARCHAR(150) NOT NULL,
                tipo VARCHAR(80) NOT NULL,
                detalle VARCHAR(500) NOT NULL,
                estado VARCHAR(30) NOT NULL DEFAULT 'Recibida'
            )
            """,
        )
        conn.commit()
    finally:
        conn.close()
