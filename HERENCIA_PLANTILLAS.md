# HERENCIA DE PLANTILLAS CON JINJA2

## 🎯 ARQUITECTURA DE PLANTILLAS

### Estructura Base (base.html)

La plantilla base contiene la estructura HTML común que se repite en todas las páginas:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}ARENILLAS VUELVE A BRILLAR-8{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
    {% block extra_css %}{% endblock %}
</head>
<body>
    <header class="bg-primary text-white">
        <!-- Header común -->
    </header>

    <nav class="navbar navbar-expand-lg navbar-dark bg-warning sticky-top">
        <!-- Navbar común -->
    </nav>

    <main class="container py-4">
        {% block content %}{% endblock %}  <!-- Contenido específico de cada página -->
    </main>

    <footer class="bg-dark text-white text-center py-3">
        <!-- Footer común -->
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="{{ url_for('static', filename='js/script.js') }}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

## 📋 BLOQUES JINJA2 DISPONIBLES

### 1. `{% block title %}`
Define el título de cada página
```html
{% block title %}Alcaldía - ARENILLAS VUELVE A BRILLAR{% endblock %}
```

### 2. `{% block extra_css %}`
Para agregar CSS adicional específico de la página
```html
{% block extra_css %}
    <style>
        /* Estilos personalizados */
    </style>
{% endblock %}
```

### 3. `{% block content %}`
Contenido principal específico de cada página
```html
{% block content %}
    <section>
        <!-- Contenido único de la página -->
    </section>
{% endblock %}
```

### 4. `{% block extra_js %}`
Para agregar JavaScript adicional específico
```html
{% block extra_js %}
    <script>
        // JavaScript personalizado
    </script>
{% endblock %}
```

## 🔄 EJEMPLO DE HERENCIA

### Plantilla Base (base.html)
```html
<html>
    <header>COMÚN</header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>COMÚN</footer>
</html>
```

### Plantilla Derivada (alcaldia.html)
```html
{% extends "base.html" %}

{% block title %}Alcaldía - ARENILLAS{% endblock %}

{% block content %}
    <h1>Alcaldía de Arenillas</h1>
    <p>Contenido específico de la página...</p>
{% endblock %}
```

### Resultado Final
```html
<html>
    <header>COMÚN</header>
    <main>
        <h1>Alcaldía de Arenillas</h1>
        <p>Contenido específico de la página...</p>
    </main>
    <footer>COMÚN</footer>
</html>
```

## ✨ VENTAJAS DE ESTA ESTRUCTURA

1. **DRY (Don't Repeat Yourself)**
   - ✅ Header, navbar y footer se definen una sola vez
   - ✅ No hay duplicación de código HTML

2. **Mantenibilidad**
   - ✅ Cambios globales en base.html afectan todas las páginas
   - ✅ Fácil actualización de navegación y estilos

3. **Consistencia**
   - ✅ Todas las páginas tienen el mismo diseño base
   - ✅ Experiencia de usuario uniforme

4. **Flexibilidad**
   - ✅ Cada página puede agregar CSS/JS específico
   - ✅ Títulos personalizados automáticamente

5. **Escalabilidad**
   - ✅ Fácil agregar nuevas páginas
   - ✅ Solo necesita la herencia y el contenido

## 📂 FLUJO DE DATOS

```
Usuario accede a /alcaldia
    ↓
Flask ejecuta: return render_template("alcaldia.html")
    ↓
Jinja2 carga alcaldia.html
    ↓
Lee: {% extends "base.html" %}
    ↓
Carga base.html
    ↓
Reemplaza {% block content %} con contenido de alcaldia.html
    ↓
Reemplaza {% block title %} con título de alcaldia.html
    ↓
Devuelve HTML completo al navegador
```

## 🔍 VERIFICACIÓN DE HERENCIA

Todas las plantillas contienen:

```html
{% extends "base.html" %}

{% block title %}[Título Específico]{% endblock %}

{% block content %}
    [Contenido específico]
{% endblock %}
```

## 📊 TABLA DE PLANTILLAS

| Archivo | Ruta | Título | Estado |
|---------|------|--------|--------|
| index.html | / | ARENILLAS VUELVE A BRILLAR-8 | ✅ |
| alcaldia.html | /alcaldia | Alcaldía | ✅ |
| municipio.html | /municipio | Municipio | ✅ |
| obras.html | /obras | Obras | ✅ |
| obras_por_registrar.html | /obras_por_registrar | Obras por Registrar | ✅ |
| noticias.html | /noticias | Noticias | ✅ |
| tramites.html | /tramites | Trámites | ✅ |
| servicios.html | /servicios | Servicios | ✅ |
| turismo.html | /turismo | Turismo | ✅ |
| contactos.html | /contactos | Contacto | ✅ |

**Todas las plantillas heredan correctamente de base.html** ✅
