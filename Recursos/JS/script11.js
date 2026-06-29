const formulario = document.getElementById("formObra");
const listaObras = document.getElementById("listaObras");
const mensaje = document.getElementById("mensaje");
const totalObras = document.getElementById("totalObras");

let contador = 0;

formulario.addEventListener("submit", function(event){

    event.preventDefault();

    const nombre = document.getElementById("nombreObra").value.trim();
    const descripcion = document.getElementById("descripcionObra").value.trim();
    const tipo = document.getElementById("tipoObra").value.trim();

    if(nombre === "" || descripcion === "" || tipo === ""){
        mensaje.innerHTML =
        "<p style='color:red;'>Todos los campos son obligatorios.</p>";
        return;
    }

    mensaje.innerHTML =
    "<p style='color:green;'>Obra registrada correctamente.</p>";

    const tarjeta = document.createElement("div");
    tarjeta.classList.add("obra");

    const titulo = document.createElement("h3");
    titulo.textContent = nombre;

    const detalle = document.createElement("p");
    detalle.textContent = descripcion;

    const categoria = document.createElement("p");
    categoria.textContent = "Tipo de obra: " + tipo;

    const botonEliminar = document.createElement("button");
    botonEliminar.textContent = "Eliminar";

    botonEliminar.addEventListener("click", function(){
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
});

