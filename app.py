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

# Conexión a PostgreSQL robusta (Evita problemas con espacios y mantiene compatibilidad con Render)
def get_db_connection():
    DATABASE_URL = os.environ.get('DATABASE_URL')
    if DATABASE_URL:
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    else:
        conn = psycopg2.connect(
            host=os.getenv('POSTGRES_HOST', 'localhost'),
            port=os.getenv('POSTGRES_PORT', '5432'),
            dbname=os.getenv('POSTGRES_DATABASE', 'ARENILLAS_VUELVE_A_BRILLAR'),
            user=os.getenv('POSTGRES_USER', 'postgres'),
            password=os.getenv('POSTGRES_PASSWORD', 'postgres')
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
    cursor.execute("SELECT * FROM usuarios WHERE id = %s OR id_usuario = %s", (user_id, user_id))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        user_id_value = user['id_usuario'] if 'id_usuario' in user.keys() else user['id']
        email_value = user['correo'] if 'correo' in user.keys() else user['email']
        rol_value = user['rol'] if 'rol' in user.keys() else 'Usuario'
        return User(user_id_value, email_value, rol_value)
    return None

# --- RUTAS DE AUTENTICACIÓN ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * FROM usuarios WHERE correo = %s OR email = %s", (correo, correo))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user:
            stored_password = user.get('password')
            user_id_value = user['id_usuario'] if 'id_usuario' in user.keys() else user['id']
            email_value = user['correo'] if 'correo' in user.keys() else user['email']
            rol_value = user['rol'] if 'rol' in user.keys() else 'Usuario'

            if stored_password and (check_password_hash(stored_password, password) or stored_password == password):
                user_obj = User(user_id_value, email_value, rol_value)
                login_user(user_obj)
                flash('Inicio de sesión exitoso.', 'success')
                return redirect(url_for('listar_obras'))
            elif stored_password is None and user.get('email') == correo:
                user_obj = User(user_id_value, email_value, rol_value)
                login_user(user_obj)
                flash('Inicio de sesión exitoso.', 'success')
                return redirect(url_for('listar_obras'))

        flash('Correo o contraseña incorrectos.', 'danger')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada correctamente.', 'info')
    return redirect(url_for('login'))

# --- PÁGINAS Y RUTAS DE COMPATIBILIDAD CON LAS PLANTILLAS ---
@app.route('/')
def hello():
    return listar_obras()

@app.route('/inicio')
@login_required
def inicio():
    return listar_obras()

@app.route('/listar_obras')
@login_required
def listar_obras():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    try:
        cursor.execute("""
            SELECT o.id, o.nombre, o.tipo, o.descripcion, o.ubicacion, o.presupuesto, o.estado, u.nombre AS responsable
            FROM obras o
            LEFT JOIN usuarios u ON o.responsable_id = u.id
            ORDER BY o.id DESC;
        """)
        obras = cursor.fetchall()
    except Exception:
        obras = []
    finally:
        cursor.close()
        conn.close()

    return render_template(
        'index.html',
        obras=obras,
        bienvenida='Bienvenido al sistema',
        municipio={'nombre': 'Arenillas', 'habitantes': '50.000', 'provincia': 'El Oro'},
        servicios_destacados=[
            {'nombre': 'Obras viales', 'descripcion': 'Mantenimiento y mejora de caminos y carreteras.', 'estado': 'Activa'},
            {'nombre': 'Infraestructura', 'descripcion': 'Mejora de espacios públicos y servicios básicos.', 'estado': 'En revisión'},
            {'nombre': 'Transparencia', 'descripcion': 'Información pública y seguimiento de proyectos.', 'estado': 'Activa'}
        ]
    )

@app.route('/alcaldia')
def alcaldia():
    return render_template('alcaldia.html')

@app.route('/municipio')
def municipio():
    return render_template('municipio.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/noticias')
def noticias():
    return render_template('noticias.html')

@app.route('/contactos')
def contactos():
    return render_template('contactos.html')

@app.route('/turismo')
def turismo():
    return render_template('turismo.html')

@app.route('/tramites')
def tramites():
    return render_template('tramites.html')

@app.route('/obras')
def obras():
    return render_template('obras.html', obras_list=[])

@app.route('/obras_por_registrar')
def obras_por_registrar():
    return render_template('obras_por_registrar.html')

@app.route('/proveedores')
def proveedores():
    return render_template('proveedores.html')

@app.route('/facturacion')
def facturacion():
    return render_template('facturacion.html')

@app.route('/nuevo_proveedor')
def nuevo_proveedor():
    return render_template('proveedores_form.html')

@app.route('/nueva_factura')
def nueva_factura():
    return render_template('facturacion_form.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

@app.route('/nuevo_cliente')
def nuevo_cliente():
    return render_template('clientes_form.html')

@app.route('/solicitar_tramite', methods=['POST'])
def solicitar_tramite():
    flash('Solicitud enviada correctamente.', 'success')
    return redirect(url_for('tramites'))

# --- OPERACIONES CRUD Y CONSULTA CON JOIN ---

# 1. LEER (SELECT con JOIN entre obras_municipales, categorias_obras y usuarios)

# 2. CREAR (INSERT con consultas parametrizadas)
@app.route('/agregar', methods=['GET', 'POST'])
@login_required
def agregar_obra():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if request.method == 'POST':
        nombre = request.form.get('titulo') or request.form.get('nombre')
        tipo = request.form.get('tipo') or 'General'
        descripcion = request.form.get('descripcion') or 'Sin descripción'
        ubicacion = request.form.get('ubicacion')
        presupuesto = request.form.get('presupuesto')
        responsable_id = current_user.id

        cursor.execute("""
            INSERT INTO obras (nombre, tipo, descripcion, ubicacion, presupuesto, estado, responsable_id)
            VALUES (%s, %s, %s, %s, %s, 'Registrada', %s)
        """, (nombre, tipo, descripcion, ubicacion, presupuesto, responsable_id))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Obra registrada exitosamente.', 'success')
        return redirect(url_for('listar_obras'))

    cursor.close()
    conn.close()
    return render_template('agregar.html')

# 3. ACTUALIZAR (UPDATE)
@app.route('/editar/<int:obra_id>', methods=['GET', 'POST'])
@login_required
def editar_obra(obra_id):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    if request.method == 'POST':
        nombre = request.form.get('titulo') or request.form.get('nombre')
        tipo = request.form.get('tipo') or 'General'
        descripcion = request.form.get('descripcion') or 'Sin descripción'
        ubicacion = request.form.get('ubicacion')
        presupuesto = request.form.get('presupuesto')

        cursor.execute("""
            UPDATE obras
            SET nombre = %s, tipo = %s, descripcion = %s, ubicacion = %s, presupuesto = %s
            WHERE id = %s
        """, (nombre, tipo, descripcion, ubicacion, presupuesto, obra_id))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Obra actualizada correctamente.', 'success')
        return redirect(url_for('listar_obras'))

    cursor.execute("SELECT * FROM obras WHERE id = %s", (obra_id,))
    obra = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('editar.html', obra=obra)

# 4. ELIMINAR (DELETE)
@app.route('/eliminar/<int:obra_id>', methods=['POST'])
@login_required
def eliminar_obra(obra_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM obras WHERE id = %s", (obra_id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash('Obra eliminada del sistema.', 'warning')
    return redirect(url_for('listar_obras'))

if __name__ == '__main__':
    app.run(debug=True)
