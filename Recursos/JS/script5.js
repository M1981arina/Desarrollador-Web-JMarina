function cambiartexto() {
    document.getElementById("titulo").innerHTML = "cambiar el texto";
}

funtion nombre() {
    let nombre = document.getElementById("nombreInput").value;
    console.log(nombre);
    document.getElementById("nombre").innerHTML = "Hola, " + nombre + "!";
    
