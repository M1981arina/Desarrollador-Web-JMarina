const formulario = document.getElementById("formObra");
const listaObras = document.getElementById("listaObras");
const mensaje = document.getElementById("mensaje");
const totalObras = document.getElementById("totalObras");
const tipoObra = document.getElementById("tipoObra");

let obras = [];

function mostrarObras() {
    if (obras.length === 0) {
        listaObras.innerHTML = `
            <div class="alert alert-warning">
                No existen obras registradas.
            </div>
        `;
        totalObras.textContent = "0";
        return;
    }

    listaObras.innerHTML = "";

    obras.forEach(function(obra, i) {
        listaObras.innerHTML += `
            <div class="card p-3">
                <h4>${obra.nombre}</h4>
                <p>${obra.descripcion}</p>
                <span class="badge bg-info text-dark">${obra.tipo}</span>
                <button type="button" class="btn btn-danger btn-sm mt-3" onclick="eliminarObra(${i})">Eliminar</button>
            </div>
        `;
    });

    totalObras.textContent = obras.length;
}

function eliminarObra(i) {
    obras.splice(i, 1);
    mostrarObras();
}

if (formulario) {
    formulario.addEventListener("submit", function(event) {
        event.preventDefault();

        const nombre = document.getElementById("nombreObra").value.trim();
        const descripcion = document.getElementById("descripcionObra").value.trim();
        const tipo = tipoObra ? tipoObra.value.trim() : "";

        if (nombre === "" || descripcion === "" || tipo === "") {
            mensaje.innerHTML = "<p style='color:red;'>Todos los campos son obligatorios.</p>";
            return;
        }

        mensaje.innerHTML = "<p style='color:green;'>Obra registrada correctamente.</p>";

        const nuevaObra = {
            nombre: nombre,
            descripcion: descripcion,
            tipo: tipo
        };

        obras.push(nuevaObra);
        mostrarObras();
        formulario.reset();
    });
}

if (tipoObra) {
    tipoObra.addEventListener("change", function() {
        if (tipoObra.value === "") {
            mensaje.innerHTML = "<p style='color:red;'>Seleccione un tipo de obra.</p>";
        } else {
            mensaje.innerHTML = "";
        }
    });
}

mostrarObras();
