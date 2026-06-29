const formulario = document.getElementById("formRegistro");
const lista = document.getElementById("listaRegistros");
const mensaje = document.getElementById("mensaje");
const total = document.getElementById("totalRegistros");

let contador = 0;

formulario.addEventListener("submit", function(event) {

    event.preventDefault();

    const nombre = document.getElementById("nombre").value.trim();
    const descripcion = document.getElementById("descripcion").value.trim();
    const categoria = document.getElementById("categoria").value.trim();

    if(nombre === "" || descripcion === "" || categoria === ""){

        mensaje.innerHTML =
        `<div class="alert alert-danger">
            Todos los campos son obligatorios.
        </div>`;

        return;
    }

    mensaje.innerHTML =
    `<div class="alert alert-success">
        Registro agregado correctamente.
    </div>`;

    const tarjeta = document.createElement("div");
    tarjeta.className = "card p-3 mb-3 shadow";

    tarjeta.innerHTML = `
        <h5>${nombre}</h5>
        <p>${descripcion}</p>
        <p><strong>Categoría:</strong> ${categoria}</p>
    `;

    const botonEliminar = document.createElement("button");
    botonEliminar.textContent = "Eliminar";
    botonEliminar.className = "btn btn-danger";

    botonEliminar.addEventListener("click", function(){
        lista.removeChild(tarjeta);
        contador--;
        total.textContent = contador;
    });

    tarjeta.appendChild(botonEliminar);

    lista.appendChild(tarjeta);

    contador++;
    total.textContent = contador;

    formulario.reset();
});