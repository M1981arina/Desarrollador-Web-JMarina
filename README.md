# Desarrollador-Web-JMarina

## Configuración PostgreSQL

La aplicación puede utilizar PostgreSQL mediante `db.py` y `psycopg2-binary`.
La contraseña se configura fuera del código:

```powershell
$env:POSTGRES_HOST = "localhost"
$env:POSTGRES_PORT = "5432"
$env:POSTGRES_DATABASE = "ARENILLAS VUELVE A BRILLAR"
$env:POSTGRES_USER = "postgres"
$env:POSTGRES_PASSWORD = "tu_clave_actual"
python app.py
```

Cuando existe `POSTGRES_HOST`, el CRUD de obras usa PostgreSQL. Puedes ejecutar `sql/esquema_postgresql.sql` en la base de datos o dejar que `init_db()` cree las tablas.

## Configuración MySQL

La aplicación utiliza `mysql-connector-python` cuando existe la variable `MYSQL_HOST`.
Antes de iniciar Flask, crea la base de datos ejecutando `sql/esquema.sql` en MySQL y configura:

```powershell
$env:MYSQL_HOST = "localhost"
$env:MYSQL_PORT = "3306"
$env:MYSQL_DATABASE = "arenillas"
$env:MYSQL_USER = "root"
$env:MYSQL_PASSWORD = "tu_clave"
python app.py
```

Sin `MYSQL_HOST`, el proyecto conserva SQLite como respaldo local para desarrollo.
El módulo `obras` permite listar, agregar, modificar y eliminar registros mediante Flask-WTF.