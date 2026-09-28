import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import psycopg2.extras

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesiones'

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Conexión a PostgreSQL (Compatible con local y con la variable de entorno de Render)
def get_db_connection():
    DATABASE_URL = os.environ.get('DATABASE_URL')
    if DATABASE_URL:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    else:
        # Tus credenciales locales exactas de PostgreSQL
        conn = psycopg2.connect(
            host="localhost",
            database="ARENILLAS VUELVE A BRILLAR",
            user="postgres",
            password="tu_password_local" # Reemplaza con tu contraseña de PostgreSQL
        )
    return conn

class User(UserMixin):
    def __init__(self, id_usuario, correo, rol):
        self.id = id_usuario
        self.correo = correo
        self.rol = rol

@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        return User(user['id_usuario'], user['correo'], user['rol'])
    return None

# --- RUTAS DE AUTENTICACIÓN ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and check_password_hash(user['password'], password):
            user_obj = User(user['id_usuario'], user['correo'], user['rol'])
            login_user(user_obj)
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('listar_obras'))
        else:
            flash('Correo o contraseña incorrectos.', 'danger')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('login'))

# --- OPERACIONES CRUD Y CONSULTA CON JOIN ---

# 1. LEER (SELECT con JOIN entre obras_municipales, categorias_obras y usuarios)
@app.route('/')
@login_required
def listar_obras():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute("""
        SELECT o.id_obra, o.titulo, o.ubicacion, o.presupuesto, c.nombre_categoria, u.nombres
        FROM obras_municipales o
        JOIN categorias_obras c ON o.id_categoria = c.id_categoria
        JOIN usuarios u ON o.id_usuario = u.id_usuario
        ORDER BY o.id_obra DESC;
    """)
    obras = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', obras=obras)

# 2. CREAR (INSERT con consultas parametrizadas)
@app.route('/agregar', methods=['GET', 'POST'])
@login_required
def agregar_obra():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if request.method == 'POST':
        titulo = request.form['titulo']
        ubicacion = request.form['ubicacion']
        presupuesto = request.form['presupuesto']
        id_categoria = request.form['id_categoria']
        id_usuario = current_user.id  # Usuario logueado actual

        cursor.execute("""
            INSERT INTO obras_municipales (titulo, ubicacion, presupuesto, id_categoria, id_usuario)
            VALUES (%s, %s, %s, %s, %s)
        """, (titulo, ubicacion, presupuesto, id_categoria, id_usuario))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Obra registrada exitosamente.', 'success')
        return redirect(url_for('listar_obras'))

    cursor.execute("SELECT * FROM categorias_obras;")
    categorias = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('agregar.html', categorias=categorias)

# 3. ACTUALIZAR (UPDATE)
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_obra(id):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if request.method == 'POST':
        titulo = request.form['titulo']
        ubicacion = request.form['ubicacion']
        presupuesto = request.form['presupuesto']
        id_categoria = request.form['id_categoria']

        cursor.execute("""
            UPDATE obras_municipales
            SET titulo = %s, ubicacion = %s, presupuesto = %s, id_categoria = %s
            WHERE id_obra = %s
        """, (titulo, ubicacion, presupuesto, id_categoria, id))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Obra actualizada correctamente.', 'success')
        return redirect(url_for('listar_obras'))

    cursor.execute("SELECT * FROM obras_municipales WHERE id_obra = %s", (id,))
    obra = cursor.fetchone()
    cursor.execute("SELECT * FROM categorias_obras;")
    categorias = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('editar.html', obra=obra, categorias=categorias)

# 4. ELIMINAR (DELETE)
@app.route('/eliminar/<int:id>')
@login_required
def eliminar_obra(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM obras_municipales WHERE id_obra = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash('Obra eliminada del sistema.', 'warning')
    return redirect(url_for('listar_obras'))

if __name__ == '__main__':
    app.run(debug=True)
