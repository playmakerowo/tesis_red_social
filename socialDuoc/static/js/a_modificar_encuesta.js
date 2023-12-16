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
            text: "Encuesta modificada",
        });
    }
});