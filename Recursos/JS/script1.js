const formulario = document.getElementById("formulario");
const mensaje = document.getElementById("mensaje");

formulario.addEventListener("submit", function(event) {
    event.preventDefault(); // Evitar el envío del formulario por defecto
    let nombre = document.getElementById("nombreInput").value;
    let categoria = document.getElementById("categoriaInput").value;
    Console.log("Nombre, descripcion, categoria);

    if (nombre==="" || categoria === "") {
        mensaje.innerHTML = "Por favor, complete todos los campos.";
        llene el campo
<div>;
    }
     