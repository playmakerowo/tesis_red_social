//Alerta de SWAL
document.addEventListener("DOMContentLoaded", function () {
    // Obtén todos los elementos con el atributo "name" igual a "eliminar-btn"
    var botonesEliminar = document.querySelectorAll("[name='eliminar-btn']");

    // Agregar un evento clic a cada botón
    botonesEliminar.forEach(function (boton) {
        boton.addEventListener("click", function (e) {
            e.preventDefault(); // Evita que el enlace se siga

            // Mostrar la alerta SweetAlert
            Swal.fire({
                title: 'Seguro que desea eliminar al usuario?',
                text: "Una vez eliminado no se podra recuperar su informacion",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Eliminar',
                cancelButtonText: 'Cancelar'
            })
        });
    });
});

function actualizarInterfazUsuario() {
    // Tu lógica para actualizar la interfaz de usuario aquí
}

function eliminarUsuario(csrfToken, userId) {
    // Realiza una solicitud AJAX al servidor para eliminar al usuario sin recargar la página.
    fetch('/eliminar-usuario/', {
        method: 'POST',
        body: JSON.stringify({ id: userId }),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        }
    })
    .then(response => {
        console.log(response);
        if (response.ok) {
            // El usuario fue eliminado con éxito, puedes realizar acciones adicionales si es necesario.
            // Por ejemplo, actualizar la interfaz de usuario sin recargar la página.
            actualizarInterfazUsuario();
            console.log("holaa" + userId)
        } else {
            // Manejar errores si la eliminación del usuario falla.
            console.error('Error al eliminar usuario.');
        }
    })
    .catch(error => {
        console.error('Error en la solicitud AJAX:', error);
    });
}




