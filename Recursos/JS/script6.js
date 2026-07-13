const formulario = document.getElementById("formObra");
const listaObras = document.getElementById("listaObras");
const mensaje = document.getElementById("mensaje");
const totalObras = document.getElementById("totalObras");

const nombre = document.getElementById("nombreObra");
const descripcion = document.getElementById("descripcionObra");
const tipo = document.getElementById("tipoObra");

let contador = 0;

/* =========================
   VALIDACIONES EN TIEMPO REAL
========================= */

nombre.addEventListener("input", validarNombre);
nombre.addEventListener("blur", validarNombre);

descripcion.addEventListener("input", validarDescripcion);
descripcion.addEventListener("blur", validarDescripcion);

tipo.addEventListener("change", validarTipo);

/* =========================
   FUNCIONES DE VALIDACIÓN
========================= */

function validarNombre() {
    if (nombre.value.trim().length < 5) {
        nombre.classList.add("is-invalid");
        nombre.classList.remove("is-valid");
        return false;
    } else {
        nombre.classList.add("is-valid");
        nombre.classList.remove("is-invalid");
        return true;
    }
}

function validarDescripcion() {
    if (descripcion.value.trim().length < 10) {
        descripcion.classList.add("is-invalid");
        descripcion.classList.remove("is-valid");
        return false;
    } else {
        descripcion.classList.add("is-valid");
        descripcion.classList.remove("is-invalid");
        return true;
    }
}

function validarTipo() {
    if (tipo.value === "") {
        tipo.classList.add("is-invalid");
        tipo.classList.remove("is-valid");
        return false;
    } else {
        tipo.classList.add("is-valid");
        tipo.classList.remove("is-invalid");
        return true;
    }
}

/* =========================
   SUBMIT DEL FORMULARIO
========================= */

formulario.addEventListener("submit", function(event) {

    event.preventDefault();

    const v1 = validarNombre();
    const v2 = validarDescripcion();
    const v3 = validarTipo();

    if (!v1 || !v2 || !v3) {
        mensaje.innerHTML = `
            <div class="alert alert-danger">
                Por favor complete correctamente todos los campos.
            </div>
        `;
        return;
    }

    mensaje.innerHTML = `
        <div class="alert alert-success">
            Obra registrada correctamente.
        </div>
    `;

    const tarjeta = document.createElement("div");
    tarjeta.classList.add("card", "p-3", "mb-2");

    const titulo = document.createElement("h5");
    titulo.textContent = nombre.value;

    const detalle = document.createElement("p");
    detalle.textContent = descripcion.value;

    const categoria = document.createElement("span");
    categoria.classList.add("badge", "bg-info");
    categoria.textContent = "Tipo: " + tipo.value;

    const botonEliminar = document.createElement("button");
    botonEliminar.textContent = "Eliminar";
    botonEliminar.classList.add("btn", "btn-danger", "btn-sm", "mt-2");

    botonEliminar.addEventListener("click", function() {
        listaObras.removeChild(tarjeta);
        contador--;
        totalObras.textContent = contador;
    });

    tarjeta.appendChild(titulo);
    tarjeta.appendChild(detalle);
    tarjeta.appendChild(categoria);
    tarjeta.appendChild(botonEliminar);

    listaObras.appendChild(tarjeta);

    contador++;
    totalObras.textContent = contador;

    formulario.reset();

    nombre.classList.remove("is-valid");
    descripcion.classList.remove("is-valid");
    tipo.classList.remove("is-valid");
});