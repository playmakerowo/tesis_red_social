$(document).ready(function () {
    
$('#select_carrera').select2();
$('#select_ramo').select2();

function verificarCampos() {
    var selectedCarrera = $('#select_carrera').val();
    var selectedRamo = $('#select_ramo').val();
    var nombreSeccionInput = $('#nombre_seccion');
    var botonCrear = $('#boton_crear');

    // Verificar campos y habilitar/deshabilitar el botón
    if (selectedCarrera && selectedRamo && nombreSeccionInput.val().trim() !== "") {
        $('#incompleto').hide();
        botonCrear.prop('disabled', false);
    } else {
        $('#incompleto').show();
        botonCrear.prop('disabled', true);
    }
}
// Agregar evento click para el botón de crear

$('#select_carrera').on('change', function () {
    var selectedCarrera = $(this).val();
    var selectRamo = $('#select_ramo');

    // Limpiar opciones actuales
    selectRamo.empty();

    // Agregar opción por defecto
    selectRamo.append('<option value="" selected disabled>Selecciona un ramo</option>');

    // Filtrar y agregar opciones correspondientes a la carrera seleccionada
    ramos.forEach(function (ramo) {
        if (ramo.id_carrera == selectedCarrera || ramo.id_carrera == undefined) {
            selectRamo.append('<option value="' + ramo.id_ramo + '" data-id-carrera="' + ramo.id_carrera + '">' + ramo.nombre +'</option>');
        }
    });

    // Actualizar el select2
    selectRamo.trigger('change');

    // Habilitar o deshabilitar el selectRamo según si se ha seleccionado una carrera
    if (selectedCarrera) {
        $('#requerido_carrera').hide();
        selectRamo.prop('disabled', false);
    } else {
        $('#requerido_carrera').show();
        selectRamo.prop('disabled', true);
    }

    // Verificar campos
    verificarCampos();
});

$('#select_ramo').on('change', function () {
    // Habilitar o deshabilitar el input del nombre de la sección según si se ha seleccionado un ramo
    var selectedRamo = $(this).val();
    var nombreSeccionInput = $('#nombre_seccion');

    if (selectedRamo) {
        $('#requerido_ramo').hide();
        nombreSeccionInput.prop('disabled', false);
    } else {
        $('#requerido_ramo').show();
        nombreSeccionInput.prop('disabled', true);
    }
    // Verificar campos
    verificarCampos();
});

// Agregar evento input para el campo de nombre de sección
$('#nombre_seccion').on('input', function () {
    // Verificar campos
    verificarCampos();
});

$('#agregar_seccion').on('submit', function (e) {
    e.preventDefault();
    var form = $(this);
    var id_ramo = $('#select_ramo').val();
    var nombre_seccion = $('#nombre_seccion').val();
    console.log('Formulario enviado' + ' ramo:' + id_ramo + ' seccion:' + nombre_seccion);
    // Realiza una solicitud AJAX para agregar el comentario
    $.ajax({
        type: "POST",
        url: "/form_seccion_crear",
        data: {
            id_ramo: id_ramo,
            nombre_seccion: nombre_seccion,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            console.log(data);
            if (data.success === 'EXITO') {
                Swal.fire({
                    icon: 'success',
                    title: 'Exito',
                    html: 'Seccion Creada <a href="/secciones" style="color:blue">Ver secciones</a>',
                    confirmButtonText: `Cerrar`,
                });
                $('#select_carrera').val('').trigger('change'); // Limpiar select de carreras
                $('#select_ramo').val('').trigger('change'); // Limpiar select de ramos
                $('#nombre_seccion').val('');
            } else if (data.error) {
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: 'Hubo un error al procesar la solicitud. Detalles: ' + data.error,
                });
            }
        },
        error: function (response, status, error) {
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Hubo un error al procesar la solicitud. Detalles: ' + error + data.error,
            });
        }
    });
});
});