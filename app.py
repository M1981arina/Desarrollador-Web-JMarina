from flask import Flask, render_template, redirect, url_for, flash

from forms.clientes import ClienteForm
from forms.facturacion import FacturaForm
from forms.productos import ProductoForm
from forms.proveedores import ProveedorForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "arenillas-secret-key-2026"

productos_db = [
    {"id": 1, "nombre": "Rehabilitación de la avenida central", "tipo": "Vial", "encargado": "Dirección de Obras", "avance": 82, "estado": "En ejecución"},
    {"id": 2, "nombre": "Mejoramiento del parque municipal", "tipo": "Espacio público", "encargado": "Área de Parques", "avance": 65, "estado": "En revisión"},
    {"id": 3, "nombre": "Sistema de agua potable", "tipo": "Servicio básico", "encargado": "Departamento de Agua", "avance": 90, "estado": "Finalizado"},
]

clientes_db = [
    {"id": 1, "nombre": "Ana Torres", "email": "ana@correo.com", "telefono": "0987654321", "cedula": "0950000001"},
    {"id": 2, "nombre": "Carlos Ponce", "email": "carlos@correo.com", "telefono": "0981112233", "cedula": "0950000002"},
]

proveedores_db = [
    {"id": 1, "nombre": "María López", "tramite": "Permiso de construcción", "email": "maria.lopez@correo.com", "telefono": "0999988777", "estado": "Activo"},
    {"id": 2, "nombre": "Carlos Aguirre", "tramite": "Registro civil", "email": "carlos.aguirre@correo.com", "telefono": "0988776655", "estado": "En espera"},
]

facturas_db = [
    {"id": 1, "cliente": "Ana Torres", "subtotal": 120.00, "iva": 18.00, "total": 138.00, "estado": "Pagada"},
    {"id": 2, "cliente": "Carlos Ponce", "subtotal": 85.50, "iva": 12.83, "total": 98.33, "estado": "Pendiente"},
]


@app.context_processor
def inject_global_context():
    return {
        "site_name": "ARENILLAS",
        "year": 2026,
    }


@app.route('/')
def hello():
    municipio = {
        "nombre": "Arenillas",
        "provincia": "El Oro",
        "habitantes": 46000,
        "telefono": "+593 969280318",
    }

    servicios_destacados = [
        {"nombre": "Obras Viales", "descripcion": "Rehabilitación de calles y accesos principales.", "estado": "Activa"},
        {"nombre": "Servicios Básicos", "descripcion": "Mejoras en agua potable y alcantarillado.", "estado": "En operación"},
        {"nombre": "Espacios Públicos", "descripcion": "Parques, jardines y áreas recreativas.", "estado": "Programada"},
    ]

    return render_template(
        "index.html",
        bienvenida="Bienvenido a Arenillas Vuelve a Brillar",
        municipio=municipio,
        servicios_destacados=servicios_destacados,
    )


@app.route('/alcaldia')
def alcaldia():
    return render_template("alcaldia.html", alcaldia_info={
        "nombre": "Johanna Marina Castillo Rodriguez",
        "cargo": "Alcaldesa",
        "mensaje": "Trabajo para una ciudad más transparente, ordenada y moderna.",
    })


@app.route('/municipio')
def municipio():
    municipio_info = {
        "nombre": "Arenillas",
        "direccion": "Av. José Moncada",
        "barrios": ["Centro", "San Vicente", "La Libertad", "El Progreso"],
        "estadisticas": {
            "habitantes": 46000,
            "barrios": 12,
            "proyectos": 25,
        },
    }
    return render_template("municipio.html", municipio_info=municipio_info)


@app.route('/obras')
def obras():
    obras_list = [
        {"nombre": "Rehabilitación de la avenida principal", "tipo": "Vial", "avance": 80, "stock": 5},
        {"nombre": "Parque Central", "tipo": "Espacio público", "avance": 65, "stock": 0},
        {"nombre": "Mejoramiento del sistema de agua", "tipo": "Servicios", "avance": 90, "stock": 2},
    ]
    return render_template("obras.html", obras_list=obras_list)


@app.route('/obras_por_registrar')
def obras_por_registrar():
    return render_template("obras_por_registrar.html")


@app.route('/noticias')
def noticias():
    noticias_list = [
        {"titulo": "Apertura de talleres comunitarios", "estado": "Nuevo"},
        {"titulo": "Avance de obras viales", "estado": "Activo"},
    ]
    return render_template("noticias.html", noticias_list=noticias_list)


@app.route('/tramites')
def tramites():
    tramites_list = [
        {"nombre": "Permisos de construcción", "estado": "Disponible"},
        {"nombre": "Registro civil", "estado": "Disponible"},
    ]
    return render_template("tramites.html", tramites_list=tramites_list)


@app.route('/servicios')
def servicios():
    servicios_list = [
        {"nombre": "Agua Potable", "descripcion": "Distribución y mantenimiento del servicio.", "stock": 7},
        {"nombre": "Recolección de Basura", "descripcion": "Servicio urbano para limpieza y residuos.", "stock": 0},
        {"nombre": "Alumbrado Público", "descripcion": "Mantenimiento de luminarias y energía.", "stock": 4},
    ]
    return render_template("servicios.html", servicios_list=servicios_list)


@app.route('/turismo')
def turismo():
    turismo_list = [
        {"lugar": "Mirador del Río", "tipo": "Atractivo natural"},
        {"lugar": "Parque Central", "tipo": "Sitio histórico"},
    ]
    return render_template("turismo.html", turismo_list=turismo_list)


@app.route('/contactos')
def contactos():
    contacto = {
        "correo": "arenillasbrilla@gmail.com",
        "telefono": "+593 969280318",
        "direccion": "Avda José Moncada, Arenillas, Ecuador",
    }
    return render_template("contactos.html", contacto=contacto)


@app.route('/productos', methods=['GET'])
def productos():
    return render_template('productos.html', productos=productos_db)


@app.route('/productos/nuevo', methods=['GET', 'POST'])
def nuevo_producto():
    form = ProductoForm()
    if form.validate_on_submit():
        producto = {
            'id': len(productos_db) + 1,
            'nombre': form.nombre.data,
            'categoria': form.categoria.data,
            'precio': form.precio.data,
            'stock': form.stock.data,
        }
        productos_db.append(producto)
        flash('Producto registrado correctamente.', 'success')
        return redirect(url_for('productos'))
    return render_template('productos_form.html', form=form, titulo='Registrar obra', accion='Registrar')


@app.route('/productos/<int:producto_id>/editar', methods=['GET', 'POST'])
def editar_producto(producto_id):
    producto = next((item for item in productos_db if item['id'] == producto_id), None)
    if producto is None:
        flash('Producto no encontrado.', 'danger')
        return redirect(url_for('productos'))

    form = ProductoForm(obj=producto)
    if form.validate_on_submit():
        producto['nombre'] = form.nombre.data
        producto['categoria'] = form.categoria.data
        producto['precio'] = form.precio.data
        producto['stock'] = form.stock.data
        flash('Producto actualizado correctamente.', 'success')
        return redirect(url_for('productos'))
    return render_template('productos_form.html', form=form, titulo='Editar obra', accion='Actualizar')


@app.route('/clientes', methods=['GET'])
def clientes():
    return render_template('clientes.html', clientes=clientes_db)


@app.route('/clientes/nuevo', methods=['GET', 'POST'])
def nuevo_cliente():
    form = ClienteForm()
    if form.validate_on_submit():
        cliente = {
            'id': len(clientes_db) + 1,
            'nombre': form.nombre.data,
            'email': form.email.data,
            'telefono': form.telefono.data,
            'cedula': form.cedula.data,
        }
        clientes_db.append(cliente)
        flash('Cliente registrado correctamente.', 'success')
        return redirect(url_for('clientes'))
    return render_template('clientes_form.html', form=form, titulo='Registrar cliente', accion='Registrar')


@app.route('/clientes/<int:cliente_id>/editar', methods=['GET', 'POST'])
def editar_cliente(cliente_id):
    cliente = next((item for item in clientes_db if item['id'] == cliente_id), None)
    if cliente is None:
        flash('Cliente no encontrado.', 'danger')
        return redirect(url_for('clientes'))

    form = ClienteForm(obj=cliente)
    if form.validate_on_submit():
        cliente['nombre'] = form.nombre.data
        cliente['email'] = form.email.data
        cliente['telefono'] = form.telefono.data
        cliente['cedula'] = form.cedula.data
        flash('Cliente actualizado correctamente.', 'success')
        return redirect(url_for('clientes'))
    return render_template('clientes_form.html', form=form, titulo='Editar cliente', accion='Actualizar')


@app.route('/proveedores', methods=['GET'])
def proveedores():
    return render_template('proveedores.html', proveedores=proveedores_db)


@app.route('/proveedores/nuevo', methods=['GET', 'POST'])
def nuevo_proveedor():
    form = ProveedorForm()
    if form.validate_on_submit():
        proveedor = {
            'id': len(proveedores_db) + 1,
            'nombre': form.nombre.data,
            'contacto': form.contacto.data,
            'email': form.email.data,
            'telefono': form.telefono.data,
        }
        proveedores_db.append(proveedor)
        flash('Proveedor registrado correctamente.', 'success')
        return redirect(url_for('proveedores'))
    return render_template('proveedores_form.html', form=form, titulo='Registrar usuario', accion='Registrar')


@app.route('/proveedores/<int:proveedor_id>/editar', methods=['GET', 'POST'])
def editar_proveedor(proveedor_id):
    proveedor = next((item for item in proveedores_db if item['id'] == proveedor_id), None)
    if proveedor is None:
        flash('Proveedor no encontrado.', 'danger')
        return redirect(url_for('proveedores'))

    form = ProveedorForm(obj=proveedor)
    if form.validate_on_submit():
        proveedor['nombre'] = form.nombre.data
        proveedor['contacto'] = form.contacto.data
        proveedor['email'] = form.email.data
        proveedor['telefono'] = form.telefono.data
        flash('Proveedor actualizado correctamente.', 'success')
        return redirect(url_for('proveedores'))
    return render_template('proveedores_form.html', form=form, titulo='Editar usuario', accion='Actualizar')


@app.route('/facturacion', methods=['GET'])
def facturacion():
    return render_template('facturacion.html', facturas=facturas_db)


@app.route('/facturacion/nuevo', methods=['GET', 'POST'])
def nueva_factura():
    form = FacturaForm()
    if form.validate_on_submit():
        factura = {
            'id': len(facturas_db) + 1,
            'cliente': form.cliente.data,
            'subtotal': form.subtotal.data,
            'iva': form.iva.data,
            'total': form.total.data,
            'estado': form.estado.data,
        }
        facturas_db.append(factura)
        flash('Factura registrada correctamente.', 'success')
        return redirect(url_for('facturacion'))
    return render_template('facturacion_form.html', form=form, titulo='Registrar factura', accion='Registrar')


@app.route('/facturacion/<int:factura_id>/editar', methods=['GET', 'POST'])
def editar_factura(factura_id):
    factura = next((item for item in facturas_db if item['id'] == factura_id), None)
    if factura is None:
        flash('Factura no encontrada.', 'danger')
        return redirect(url_for('facturacion'))

    form = FacturaForm(obj=factura)
    if form.validate_on_submit():
        factura['cliente'] = form.cliente.data
        factura['subtotal'] = form.subtotal.data
        factura['iva'] = form.iva.data
        factura['total'] = form.total.data
        factura['estado'] = form.estado.data
        flash('Factura actualizada correctamente.', 'success')
        return redirect(url_for('facturacion'))
    return render_template('facturacion_form.html', form=form, titulo='Editar factura', accion='Actualizar')


if __name__ == '__main__':
    app.run(debug=True)
