//select 
$(document).ready(function () {
    $('#select_usuarios').select2();
});

//AJAX ELIMINAR PARTICIAPANTE
$(document).ready(function () {
    $('.delete-participante-btn').click(function (e) {
        e.preventDefault();

        // Obtén el ID del participante desde el atributo data
        var participante_id = $(this).data('participante-id');
        var id = $(this).data('evento-id');
        // Guarda una referencia al botón actual para ocultarlo después
        var btn = $(this);

        // Muestra un modal de confirmación
        Swal.fire({
            title: '¿Estás seguro?',
            text: 'Esta acción eliminará el participante. ¿Quieres continuar?',
            icon: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#3085d6',
            cancelButtonColor: '#d33',
            confirmButtonText: 'Sí, eliminar',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                // Si el usuario confirma, envía la solicitud AJAX para eliminar el participante
                $.ajax({
                    type: 'POST',
                    url: '/editar_evento/' + id +'/' ,  // Reemplaza con la URL adecuada en tu aplicación
                    data: {
                        participante_id: participante_id,
                        id: id,
                        accion: 'eliminar',  // Agrega la acción aquí
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                    },
                    success: function (data) {
                        // Elimina el botón y/o actualiza la interfaz según tu lógica
                        console.log("eliminado");
                        Swal.fire({
                            icon: "success",
                            title: "Eliminado",
                            text: "Participante eliminado",
                        });
                        console.log(id)
                        console.log(participante_id)
                        // Oculta el participante
                        btn.closest('div').hide();
                    },
                    error: function (xhr, status, error) {
                        Swal.fire({
                            icon: "error",
                            title: "Error",
                            text: "Error al eliminar",
                        });
                    }
                });
            }
        });
    });
});

//BUSCADOR POR PARTICIPANTES
document.addEventListener("keyup", e => {
    if (e.target.matches("#buscador")) {
        const term = e.target.value.toLowerCase();

        document.querySelectorAll(".participante-lista").forEach(elemento => {
            const textoParticipante = elemento.querySelector("a").textContent.toLowerCase();

            textoParticipante.includes(term)
                ? elemento.classList.remove("hidden")
                : elemento.classList.add("hidden");
        });
    }
});


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
            text: "Datos cargados con exito",
            footer: '<a href="/Home" style="color:blue;">Ir al Home</a>'
        });
    }

});
