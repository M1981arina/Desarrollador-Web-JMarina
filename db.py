import os

try:
    import psycopg2
except ImportError:
    psycopg2 = None


# La contrasena se proporciona mediante POSTGRES_PASSWORD y no se guarda en el codigo.
def obtener_conexion():
    if psycopg2 is None:
        raise RuntimeError("Instala psycopg2-binary para utilizar PostgreSQL.")

    try:
        return psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "localhost"),
            database=os.getenv("POSTGRES_DATABASE", "ARENILLAS VUELVE A BRILLAR"),
            user=os.getenv("POSTGRES_USER", "postgres"),
            password=os.getenv("POSTGRES_PASSWORD", ""),
            port=os.getenv("POSTGRES_PORT", "5432"),
        )
    except Exception as error:
        print(f"Error al conectar a la base de datos: {error}")
        return None
