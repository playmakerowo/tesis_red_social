$(document).on('submit','#correoForm', function(event){
    event.preventDefault();

    $("#aviso").hide();
    // Muestra el indicador de carga
    $("#loading-indicator").show();

    $.ajax({
        type:'POST',
        url: '/enviar_correo',
        data: {
            correo: $('#correo').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(data){
            $("#aviso").show();
            var h2 = $('h2');
            if (data.includes("no es valido")) {
                h2.css('color', 'red');
            } else {
                h2.css('color', 'greenyellow');
            }
            $('h2').html(data);
            $("#loading-indicator").hide();
        }
    })
})