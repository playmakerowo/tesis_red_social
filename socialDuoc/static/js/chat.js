var mensajesAnteriores = -1;
var usuario = 0;

function links() {
    // Selecciona todos los elementos con la clase 'texto' dentro de '#mensajes'

    $('#mensajes .texto').each(function () {
        var texto = $(this).text(); // Obtén el texto del elemento
        var chatPanel = $('.panel-chat');
        var scrollHeight = chatPanel[0].scrollHeight;
        // Expresión regular para encontrar enlaces en el texto
        var regexEnlace = /(https?:\/\/[^\s]+)|(www\.[^\s]+)/g;

        var textoConEnlaces = texto.replace(regexEnlace, function (enlace) {
            // Si no comienza con "http://" o "https://", añade "http://"
            if (!/^https?:\/\//i.test(enlace)) {
                enlace = "http://" + enlace;
            }

            // Intenta cargar la imagen
            var imagen = new Image();
            imagen.src = enlace;

            // Verifica si la carga de la imagen tiene éxito
            if (imagen.complete) {
                var dominio = new URL(enlace).hostname;
                // Devuelve un elemento de imagen con el enlace
                return '<a href="' + enlace + '" target="_blank" style="color: gold; font-size: 1em;">' +
       '<img src="' + enlace + '" alt="imagen" style=" max-height: 400px; max-width: 400px;"> ' + dominio + ' </a><br>';

            } else {
                // Extraer el dominio del enlace
                var dominio = new URL(enlace).hostname;
                // Crea un elemento de enlace con el dominio como texto
                return '<a href="' + enlace + '" target="_blank" style="color: gold; font-size: 1em;">' + dominio + '</a>';
            }
        });
        // Reemplaza el contenido del elemento con el nuevo texto que contiene enlaces
        $(this).html(textoConEnlaces);

    });
}

$('.usuario').on('click', function () {

    $('#mensajes').empty();

    // Obtener el ID del usuario a partir del atributo data
    var nuevoUsuario = $(this).data('usuario-id');
    usuario = nuevoUsuario;
    $('#id_usuario_recep').val(usuario);


    var chatId = $(this).closest('.usuario').find('.chat-id').val();
    $('#chatIdInput').val(chatId);

    var nombre = $(this).closest('.usuario').find('.nombre').val();
    $('#titulo_nombre').html(nombre);
    

    var chatTipo = $(this).closest('.usuario').find('.chat-Tipo').val();
    $('#tipo').val(chatTipo);

    var foto = $(this).find('.foto').val();

    // Establecer la URL de la imagen en el campo con id "foto"
    $('#foto').attr('src', foto);


    obtenerMensajes(function () {
        // Esta función se ejecuta después de cargar los mensajes
        var chatPanel = $('.panel-chat');
        var scrollHeight = chatPanel[0].scrollHeight;
        // Agrega un tiempo de espera de 5 segundos antes de realizar el scroll
        chatPanel.scrollTop(scrollHeight);
    });

});



var mensajesa = []; // Arreglo para almacenar los mensajes actuales


function obtenerMensajes(callback) {
    $.ajax({
        url: '/obtener_mensajes',
        type: "GET",
        data: { usuario_id: usuario },
        success: function (data) {
            var mensajes = data.mensajes;
            var mensajeHTML = '';

            for (var i = 0; i < mensajes.length; i++) {
                var mensaje = mensajes[i];
                mensajeHTML += '<div class="mensaje ' + mensaje.lado + '">';
                mensajeHTML += '<div class="' + mensaje.cuerpo + '" style="' + mensaje.color + '">';
                mensajeHTML += '<div class="texto">' + mensaje.mensaje + '</div>';
                mensajeHTML += '<span class="fecha">'+ mensaje.nombre_origen +'</span>';
                mensajeHTML += '</div>';
                mensajeHTML += '</div>';
            }

            $('#mensajes').html(mensajeHTML);
            var chatPanel = $('.panel-chat');
            var scrollHeight = chatPanel[0].scrollHeight;
            links();


            if (JSON.stringify(mensajesa) !== JSON.stringify(mensajes)) {
                chatPanel.scrollTop(scrollHeight);
            }

            mensajesa = mensajes; // Actualizar el arreglo con los nuevos mensajes
            if (typeof callback === 'function') {
                callback(); // Llama al callback después de cargar los mensajes
            }


        }

    });
}


// Llama a obtenerMensajes() periódicamente para actualizar el chat en tiempo real
setInterval(obtenerMensajes, 2000);


$(document).on('submit', '#msgForm', function (event) {
    event.preventDefault();


    console.log('Valor de tipo:', $('#tipo').val());
    $.ajax({
        type: 'POST',
        url: '/enviar_mensaje',
        data: {
            chatIdInput: $('#chatIdInput').val(),
            id_usuario: $('#id_usuario').val(),
            id_usuario_recep: $('#id_usuario_recep').val(),
            mensaje: $('#mensaje').val(),
            tipo: $('#tipo').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function (data) {
            obtenerMensajes(function () {
                // Esta función se ejecuta después de cargar los mensajes
                var chatPanel = $('.panel-chat');
                var scrollHeight = chatPanel[0].scrollHeight;
                chatPanel.scrollTop(scrollHeight);
                $("#mensaje").val('');
            });
        }
    })
})

document.addEventListener("keyup", e => {

    if (e.target.matches("#buscador")) {

        document.querySelectorAll(".buscar-usuarios").forEach(elemento => {
            elemento.innerText.toLowerCase().includes(e.target.value.toLowerCase())
                ? elemento.classList.remove("hidden")
                : elemento.classList.add("hidden");
        });

    }
})


