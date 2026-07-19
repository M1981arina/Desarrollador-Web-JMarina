const formulario = document.getElementById("formObra");
const listaObras = document.getElementById("listaObras");
const mensaje = document.getElementById("mensaje");
const totalObras = document.getElementById("totalObras");
const tipoObra = document.getElementById("tipoObra");
const spinner = document.getElementById("spinner");
const modalTitle = document.getElementById("modalTitle");
const modalBody = document.getElementById("modalBody");
const detalleModalEl = document.getElementById("detalleModal");
const detalleModal = detalleModalEl ? new bootstrap.Modal(detalleModalEl) : null;

let obras = [];

function mostrarAlerta(tipo, texto) {
    mensaje.innerHTML = `
        <div class="alert alert-${tipo} alert-dismissible fade show" role="alert">
            ${texto}
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Cerrar"></button>
        </div>
    `;
}

function mostrarSpinner(mostrar) {
    if (!spinner) return;
    spinner.classList.toggle("d-none", !mostrar);
}

function mostrarObras() {
    if (obras.length === 0) {
        listaObras.innerHTML = `
            <div class="col">
                <div class="alert alert-warning">No existen obras registradas.</div>
            </div>
        `;
        totalObras.textContent = "0";
        return;
    }

    listaObras.innerHTML = "";

    obras.forEach(function (obra, i) {
        listaObras.innerHTML += `
            <div class="col">
                <div class="card h-100 shadow-sm">
                    <div class="card-body">
                        <h5 class="card-title">${obra.nombre}</h5>
                        <p class="card-text">${obra.descripcion}</p>
                        <span class="badge bg-info text-dark">${obra.tipo}</span>
                    </div>
                    <div class="card-footer bg-transparent d-flex justify-content-between gap-2">
                        <button type="button" class="btn btn-primary btn-sm" onclick="abrirModalDetalle(${i})">Ver detalles</button>
                        <button type="button" class="btn btn-danger btn-sm" onclick="eliminarObra(${i})">Eliminar</button>
                    </div>
                </div>
            </div>
        `;
    });

    totalObras.textContent = obras.length;
}

function abrirModalDetalle(i) {
    const obra = obras[i];
    if (!obra || !detalleModal) return;

    modalTitle.textContent = `Detalle de: ${obra.nombre}`;
    modalBody.innerHTML = `
        <p><strong>Tipo:</strong> ${obra.tipo}</p>
        <p><strong>Descripción:</strong></p>
        <p>${obra.descripcion}</p>
        <p class="small text-muted">Registro dinámico generado desde la semana 7.</p>
    `;
    detalleModal.show();
}

function eliminarObra(i) {
    mostrarSpinner(true);
    setTimeout(() => {
        obras.splice(i, 1);
        mostrarObras();
        mostrarSpinner(false);
        mostrarAlerta("warning", "Obra eliminada correctamente.");
    }, 500);
}

if (formulario) {
    formulario.addEventListener("submit", function (event) {
        event.preventDefault();

        const nombre = document.getElementById("nombreObra").value.trim();
        const descripcion = document.getElementById("descripcionObra").value.trim();
        const tipo = tipoObra ? tipoObra.value.trim() : "";

        if (nombre === "" || descripcion === "" || tipo === "") {
            mostrarAlerta("danger", "Todos los campos son obligatorios.");
            return;
        }

        mostrarSpinner(true);
        setTimeout(() => {
            mostrarSpinner(false);
            const nuevaObra = {
                nombre: nombre,
                descripcion: descripcion,
                tipo: tipo,
            };

            obras.push(nuevaObra);
            mostrarObras();
            formulario.reset();
            mostrarAlerta("success", "Obra registrada correctamente.");
        }, 700);
    });
}

if (tipoObra) {
    tipoObra.addEventListener("change", function () {
        if (tipoObra.value === "") {
            mostrarAlerta("warning", "Seleccione un tipo de obra.");
        } else {
            mensaje.innerHTML = "";
        }
    });
}

mostrarObras();
