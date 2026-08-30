from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
