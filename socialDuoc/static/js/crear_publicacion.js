//ALERTA DE EXITO O ERROR
document.addEventListener('DOMContentLoaded', function () {
    // Ejecuta Swal si hay un mensaje de éxito
    var successMessages = document.getElementById('mensaje').value;
    if (successMessages != "EXITO") {
        Swal.fire({
            icon: "error",
            title: "Error",
            text: successMessages,
        });
    } else {
        Swal.fire({
            icon: "success",
            title: "Éxito",
            text: "Publicacion creada con exito, ahora esta pendiente de aprobacion",
            footer: '<a href="/Home" style="color:blue">Volver a Home</a>'
        });
    }

});