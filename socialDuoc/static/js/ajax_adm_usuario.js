// Agrega un controlador de clic a los botones para almacenar la acción
$('.modificar').click(function () {
    $(this).closest('form').find('button[type="submit"]').removeClass('active');
    $(this).addClass('active');
});

// Manejar el envío del formulario
$(document).on('submit', '.archivarForm', function (event) {
    event.preventDefault();

    var form = $(this); // Obtén el formulario actual
    var button = form.find('[type="submit"].active'); // Encuentra el botón dentro del formulario
    var estado = form.closest('tr').find('.estado');
    var icono = form.closest('tr').find('.icono');
    var color = form.closest('tr').find('.color');
    var accion = button.data('accion');

    Swal.fire({
        title: 'Confirmación',
        text: '¿Estás seguro de que deseas realizar esta acción?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Sí, continuar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            $.ajax({
                type: 'POST',
                url: '/archivar_usuario',
                data: {
                    id_usuario: form.find('.id_usuario').val(),
                    csrfmiddlewaretoken: form.find('input[name=csrfmiddlewaretoken]').val(),
                    accion: accion
                },
                success: function (data) {
                    if (data === 'MODIFICADO') {
                        if (button.text() === 'Archivar') {
                            button.removeClass('text-red-700 hover:text-white border-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300');
                            button.addClass('text-purple-700 hover:text-white border border-purple-700 hover:bg-purple-800 focus:ring-4 focus:outline-none focus:ring-purple-300');
                            button.text('Activar');
                            estado.text('Archivada');
                            icono.attr('d', 'M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 11.793a1 1 0 1 1-1.414 1.414L10 11.414l-2.293 2.293a1 1 0 0 1-1.414-1.414L8.586 10 6.293 7.707a1 1 0 0 1 1.414-1.414L10 8.586l2.293-2.293a1 1 0 0 1 1.414 1.414L11.414 10l2.293 2.293Z');
                            color.removeClass('text-green-500 bg-green-100').addClass('text-red-500 bg-red-100');
                        } else {
                            button.removeClass('text-purple-700 hover:text-white border border-purple-700 hover:bg-purple-800 focus:ring-4 focus:outline-none focus:ring-purple-300');
                            button.addClass('text-red-700 hover:text-white border border-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300');
                            button.text('Archivar');
                            estado.text('Activa');
                            icono.attr('d', 'M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5Zm3.707 8.207-4 4a1 1 0 0 1-1.414 0l-2-2a1 1 0 0 1 1.414-1.414L9 10.586l3.293-3.293a1 1 0 0 1 1.414 1.414Z');
                            color.removeClass('text-red-500 bg-red-100').addClass('text-green-500 bg-green-100');
                        }
                    }
                }
            });
        }
    });
});