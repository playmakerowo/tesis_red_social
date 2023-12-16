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
            text: "Evento creado con exito, ahora esta pendiente de aprobacion, ademas ya puedes agregar participantes desde tu perfil",
            footer: '<a href="/Home" style="color:blue">Volver a Home</a>'
        });
    }

});