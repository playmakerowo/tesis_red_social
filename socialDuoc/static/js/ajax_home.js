// ###########################################################
// ###########################################################
// ########################PUBLICACION########################

$(document).on('submit', '.agregar_like_publis', function (event) {
    event.preventDefault();

    var form = $(this);
    var button = form.find(".agregar_like_publis");
    var like = button.siblings('.megusta');

    var isLiked = button.data('is-liked') === 'true';

    var likeLabel = form.siblings('.megusta'); // Selecciona el contador de "Me gusta" asociado al formulario
    var likeCount = parseInt(likeLabel.data('count'));
    var cantidadLike = form.find(".contadorLikes").val();
    $.ajax({
        type: 'POST',
        url: '/agregar_like_publi',
        data: {
            id_usuario: form.find('.id_usuario').val(),
            id_publi: form.find('.id_publi').val(),
            csrfmiddlewaretoken: form.find('input[name=csrfmiddlewaretoken]').val(),
            is_liked: isLiked,
        },
        success: function (data) {
            if (isLiked) {
                button.data('is-liked', 'false');
                button.html(`
                <svg class="w-8 h-8 text-blue-900 dark:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 20">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.008 8.714c1-.097 1.96-.45 2.792-1.028a25.112 25.112 0 0 0 4.454-5.72 1.8 1.8 0 0 1 .654-.706 1.742 1.742 0 0 1 1.65-.098 1.82 1.82 0 0 1 .97 1.128c.075.248.097.51.065.767l-1.562 4.629M4.008 8.714H1v9.257c0 .273.106.535.294.728a.99.99 0 0 0 .709.301h1.002a.99.99 0 0 0 .71-.301c.187-.193.293-.455.293-.728V8.714Zm8.02-1.028h4.968c.322 0 .64.08.925.232.286.153.531.374.716.645a2.108 2.108 0 0 1 .242 1.883l-2.36 7.2c-.288.813-.48 1.354-1.884 1.354-2.59 0-5.39-1.06-7.504-1.66"/>
              </svg>
            <span class="texto-ocultable ml-2 text-xs">Me gusta</span>
                `);
                cantidadLike--;
                isLiked = false; // Actualiza la variable isLiked
                localStorage.setItem('isLiked_' + form.find('.id_publi').val(), 'false');
            } else {
                button.data('is-liked', 'true');
                button.html(`
                    <svg class="w-8 h-8 text-blue-900 dark:text-white"
                        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                        viewBox="0 0 18 20">
                        <path
                            d="M3 7H1a1 1 0 0 0-1 1v8a2 2 0 0 0 4 0V8a1 1 0 0 0-1-1Zm12.954 0H12l1.558-4.5a1.778 1.778 0 0 0-3.331-1.06A24.859 24.859 0 0 1 6 6.8v9.586h.114C8.223 16.969 11.015 18 13.6 18c1.4 0 1.592-.526 1.88-1.317l2.354-7A2 2 0 0 0 15.954 7Z" />
                    </svg>
                    <span class="ml-2 text-xs">Ya no me gusta</span>
                `); // Cambia el contenido del botón a "Ya no me gusta"
                cantidadLike++;
                isLiked = true; // Actualiza la variable isLiked
                localStorage.setItem('isLiked_' + form.find('.id_publi').val(), 'true');
            }

            // Actualiza el valor visual del contador específico
            var publisId = form.find('.contadorLikes').data('id');
            var cantidadLikeLabel = $('.cantidadLike[data-id="' + publisId + '"]');
            cantidadLikeLabel.html(cantidadLike + " Me gusta");
            // También puedes actualizar el valor del input específico si es necesario
            form.find('.contadorLikes').val(cantidadLike);

        }
    })
})

$(document).ready(function () {
    // Itera sobre los elementos .agregar_like_publis y establece su estado
    $('.agregar_like_publis').each(function () {
        var form = $(this);
        var idPubli = form.find('.id_publi').val();
        var isLiked = localStorage.getItem('isLiked_' + idPubli);
        if (isLiked === 'true') {
            var button = form.find('.agregar_like_publis');
            button.data('is-liked', 'true');
            button.html(`
            <svg class="w-8 h-8 text-blue-900 dark:text-white"
                xmlns="http://www.w3.org/2000/svg" fill="currentColor"
                viewBox="0 0 18 20">
                <path
                    d="M3 7H1a1 1 0 0 0-1 1v8a2 2 0 0 0 4 0V8a1 1 0 0 0-1-1Zm12.954 0H12l1.558-4.5a1.778 1.778 0 0 0-3.331-1.06A24.859 24.859 0 0 1 6 6.8v9.586h.114C8.223 16.969 11.015 18 13.6 18c1.4 0 1.592-.526 1.88-1.317l2.354-7A2 2 0 0 0 15.954 7Z" />
            </svg>
            <span class="ml-2 text-xs">Ya no me gusta</span>
        `);
        }
    });
});

function basura_publicacion(publicacion_id) {
    Swal.fire({
        title: '¿Desea eliminar esta publicación?',
        text: 'Se eliminará esta publicación para siempre.',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, deseo eliminarla'
    }).then((result) => {
        if (result.isConfirmed) {
            // Realizar la eliminación mediante una solicitud AJAX
            $.ajax({
                url: '/eliminar_publi/', // La URL de la vista que maneja la eliminación
                type: 'POST',
                data: {
                    'publicacion_id': publicacion_id,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function (data) {
                    // Eliminación exitosa, ocultar la publicación
                    $('.publicacion[data-id="' + publicacion_id + '"]').hide();
                    Swal.fire('Publicación eliminada con éxito', '', 'success');
                },
                error: function (error) {
                    // Manejar errores, por ejemplo, mostrar un mensaje de error
                    Swal.fire('Error al eliminar la publicación', error.responseText, 'error');
                }
            });
        }
    });
}

function archivar_publicacion(publicacion_id) {
    Swal.fire({
        title: '¿Desea archivar esta publicacion?',
        text: "No aparecera en su inicio de publicaciones.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Deseo archivarla',
        timer: 5000,
    }).then((result) => {
        if (result.isConfirmed) {
            // Realizar la eliminación mediante una solicitud AJAX
            $.ajax({
                url: '/archivar_publicacion_inicio/', // La URL de la vista que maneja la eliminación
                type: 'POST',
                data: {
                    'publicacion_id': publicacion_id,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function (data) {
                    // Eliminación exitosa, ocultar la publicación
                    $('.publicacion[data-id="' + publicacion_id + '"]').hide();
                    Swal.fire('Publicación archivada con éxito', '', 'success');
                },
                error: function (error) {
                    // Manejar errores, por ejemplo, mostrar un mensaje de error
                    Swal.fire('Error al archivar la publicación', error.responseText, 'error');
                }
            });
        }
    });
}

function basura_comentario(publicacion_id, comentario_id) {
    Swal.fire({
        title: '¿Desea eliminar este comentario?',
        text: "Se eliminará este comentario para siempre.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, Deseo eliminarlo',
    }).then((result) => {
        if (result.isConfirmed) {
            // Realizar la eliminación mediante una solicitud AJAX
            $.ajax({
                url: '/eliminar_comentario/', // La URL de la vista que maneja la eliminación
                type: 'POST',
                data: {
                    'publicacion_id': publicacion_id,
                    'comentario_id': comentario_id,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() // Incluye el token CSRF en los datos
                },
                success: function (data) {
                    // Eliminación exitosa, ocultar el comentario
                    $('.comentario[data-id="' + comentario_id + '"]').hide();
                    Swal.fire('Comentario eliminado con éxito', '', 'success');
                },
                error: function (error) {
                    // Manejar errores, por ejemplo, mostrar un mensaje de error
                    Swal.fire('Error al eliminar el comentario', error.responseText, 'error');
                }
            });
        }
    });
}

$(document).ready(function () {
    // Manejador para todos los formularios con la clase "comentForm"
    $('.seccion-publicaciones').on('submit', '.comentForm', function (e) {
        e.preventDefault();
        var form = $(this);
        // Obtén el ID de la publicación asociada a este formulario
        var postId = form.find('.id_publi').val();
        // Obtén el comentario del campo de entrada dentro de este formulario
        var comment = form.find('.comentario').val();
        //ESTO LO ESTOY MODIFICANDO PARA PROBAR
        var usuariom = form.find('.usuario').val();
        var csrf_token = $('input[name=csrfmiddlewaretoken]').val();
        var user_id = $('#user_id').val();


        // Validar que el comentario no esté en blanco o contenga solo espacios
        if (comment.trim() === '') {
            // Puedes mostrar un mensaje de error o realizar alguna acción apropiada
            alert('El comentario no puede estar en blanco.');
            return;
        }

        // Realiza una solicitud AJAX para agregar el comentario
        $.ajax({
            type: "POST",
            url: "/agregar_comentario",
            data: {
                id_publi: postId,
                comentario: comment,
                id_usuario: form.find('.id_usuario').val(),
                usuario: usuariom,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {
                console.log(data);
                if (data.success === 'EXITO') {
                    var comentarios = data.comentarios; // Obtén la lista de comentarios actualizada
                    console.log('EXITO');
                    // Encuentra la lista de comentarios de la publicación específica
                    var commentList = $("#commentList-" + postId);

                    // Limpia la sección de comentarios
                    commentList.empty();

                    // Agrega los nuevos comentarios a la lista de comentarios específica
                    //DE AQUI HACIA ABAJO DEBO CAMBIAR EL DISEÑO
                    comentarios.forEach(function (comentario) {
                        var newComment = `
                    
                        <div class="comentario justify-center w-full border border-gray-200 rounded-lg sm:p-4 md:p-4 dark:bg-gray-800 dark:border-gray-700" data-id="${comentario.id_comentario}">
                            <div class="flex items-center space-x-12 text-sm text-white-500 dark:text-gray-400">
                                <a href="/perfil_usuarios/${comentario.id_usuario}">
                                    <div class="flex flex-col items-center justify-end pr-2 " style="width: 90px;">
                                    `

                        if (comentario.imagen == '0') {
                            newComment +=
                                `<img class="rounded-full w-10 h-10" src="/static/img/user.jpg">`
                        }
                        else {
                            newComment +=
                                `<img class="rounded-full w-10 h-10" src="data:image/png;base64, ${comentario.imagen}">`
                        }
                        newComment +=
                            `  
                                    </div>
                                </a>
                                <div class="flex items-center grid grid-cols-1">
                                <div class="flex">
                                <a href="/perfil_usuarios/${comentario.id_usuario}""
                                    class="flex items-center">
                                    <p class="flex center text-sm mr-2 sm:block hidden">
                                        ${comentario.nombre}
                                    </p>
                                </a>
                                <p class="flex center text-sm text-gray-300">
                                
                                    @${comentario.usuario}
                                </p>
                            </div>
                            <div class="flex items-center col-span-2">
                                <div class="flex items-center"
                                    style="word-break: break-all;overflow-wrap:break-word;">
                                    <p class="flex center text-sm col-span-2">
                                    ${comentario.comentario}
                                    </p>
                                </div>
                            </div>
                                </div>`
                        if (user_id == comentario.id_usuario) {
                            newComment += `<div class="ml-auto"> 
                                    <form action="/eliminar_comentario/" method="post">
                                        <input name="csrfmiddlewaretoken" value="${csrf_token}"hidden>
                                        <input type="text" name="publicacion_id" id="publicacion_id" value="${comentario.id_publi}" hidden>
                                        <input type="text" name="comentario_id" id="comentario_id" value="${comentario.id_comentario}" hidden>
                                        <input name="usuario" class="usuario" value="${comentario.usuario}"
                                                        hidden>
                                        <button type="button"
                                                onclick="basura_comentario('${comentario.id_publi}', '${comentario.id_comentario}')"
                                                class="text-white m-2 bg-gradient-to-r from-red-400 to-red-600 font-medium rounded-lg px-2 py-1 text-center">
                                                <svg class="w-auto h-4" xmlns="http://www.w3.org/2000/svg"
                                                    fill="currentColor" viewBox="0 0 18 20">
                                                    <path d="M17 4h-4V2a2 2 0 0 0-2-2H7a2 2 0 0 0-2 2v2H1a1 1 0 0 0 0 2h1v12a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V6h1a1 1 0 1 0 0-2ZM7 2h4v2H7V2Zm1 14a1 1 0 1 1-2 0V8a1 1 0 0 1 2 0v8Zm4 0a1 1 0 0 1-2 0V8a1 1 0 0 1 2 0v8Z" />
                                                </svg>
                                        </button>
                                    </form>
                                </div>`
                        }

                        newComment += `</div> </div>`;
                        commentList.append(newComment);
                    });

                    form.find(".charCountPregunta").text("0 / 500");
                    // Limpia el campo de entrada
                    form.find(".comentario").val("");
                }
            }
        });
    });
});


// ###########################################################
// ###########################################################
// ########################EVENTO#############################
function basura_evento(evento_id) {
    Swal.fire({
        title: '¿Desea eliminar este evento?',
        text: "Se eliminara este evento para siempre.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Deseo eliminarlo',
        timer: 5000,
    }).then((result) => {
        if (result.isConfirmed) {
            // Realizar la eliminación mediante una solicitud AJAX
            $.ajax({
                url: '/eliminar_evento/', // La URL de la vista que maneja la eliminación
                type: 'POST',
                data: {
                    'evento_id': evento_id,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function (data) {
                    // Eliminación exitosa, ocultar la publicación
                    $('.evento[data-id="' + evento_id + '"]').hide();
                    Swal.fire('Evento eliminado con éxito', '', 'success');
                },
                error: function (error) {
                    // Manejar errores, por ejemplo, mostrar un mensaje de error
                    Swal.fire('Error al eliminar el evento', error.responseText, 'error');
                }
            });
        }
    });
}

function archivar_evento(evento_id) {
    Swal.fire({
        title: '¿Desea archivar este evento?',
        text: "No aparecera en su inicio de eventos.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Deseo archivarlo',
        timer: 5000,
    }).then((result) => {
        if (result.isConfirmed) {
            // Realizar la eliminación mediante una solicitud AJAX
            $.ajax({
                url: '/archivar_evento_inicio/', // La URL de la vista que maneja la eliminación
                type: 'POST',
                data: {
                    'evento_id': evento_id,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function (data) {
                    // Eliminación exitosa, ocultar la publicación
                    $('.evento[data-id="' + evento_id + '"]').hide();
                    Swal.fire('Evento archivado con éxito', '', 'success');
                },
                error: function (error) {
                    // Manejar errores, por ejemplo, mostrar un mensaje de error
                    Swal.fire('Error al archivar el evento', error.responseText, 'error');
                }
            });
        }
    });
}


// ###########################################################
// ###########################################################
// ########################ENCUESTA###########################
function basura_encuesta(encuesta_id) {
    Swal.fire({
        title: '¿Desea eliminar esta encuesta?',
        text: "Se eliminara esta encuesta para siempre.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Deseo eliminarla',
        timer: 5000,
    }).then((result) => {
        if (result.isConfirmed) {
            // Realizar la eliminación mediante una solicitud AJAX
            $.ajax({
                url: '/eliminar_encuesta/', // La URL de la vista que maneja la eliminación
                type: 'POST',
                data: {
                    'encuesta_id': encuesta_id,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function (data) {
                    // Eliminación exitosa, ocultar la publicación
                    $('.encuesta[data-id="' + encuesta_id + '"]').hide();
                    Swal.fire('Encuesta eliminada con éxito', '', 'success');
                },
                error: function (error) {
                    // Manejar errores, por ejemplo, mostrar un mensaje de error
                    Swal.fire('Error al eliminar la encuesta', error.responseText, 'error');
                }
            });
        }
    });
}

function archivar_encuesta(encuesta_id) {
    Swal.fire({
        title: '¿Desea archivar esta encuesta?',
        text: "No aparecera en su inicio de encuestas.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Deseo archivarla',
        timer: 5000,
    }).then((result) => {
        if (result.isConfirmed) {
            // Realizar la eliminación mediante una solicitud AJAX
            $.ajax({
                url: '/archivar_encuesta_inicio/', // La URL de la vista que maneja la eliminación
                type: 'POST',
                data: {
                    'encuesta_id': encuesta_id,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function (data) {
                    // Eliminación exitosa, ocultar la publicación
                    $('.encuesta[data-id="' + encuesta_id + '"]').hide();
                    Swal.fire('Encuesta archivada con éxito', '', 'success');
                },
                error: function (error) {
                    // Manejar errores, por ejemplo, mostrar un mensaje de error
                    Swal.fire('Error al archivar la encuesta', error.responseText, 'error');
                }
            });
        }
    });
}

$(document).ready(function () {
    $(".encuForm").submit(function (event) {
        event.preventDefault();
        var form = $(this);
        var encuId = form.find('.txtEncu').val();
        var resp = form.find('.respuesta').val();
        var ruta_imagen = $('#ruta_imagen').val();
        var nombre = $('#nombre').val();
        // Mostrar una pregunta con SweetAlert antes de enviar la respuesta
        Swal.fire({
            title: 'Confirmación',
            text: '¿Estás seguro de enviar esta respuesta?',
            icon: 'question',
            showCancelButton: true,
            confirmButtonText: 'Sí, enviar',
            cancelButtonText: 'Cancelar'
        }).then((result) => {
            if (result.isConfirmed) {
                $.ajax({
                    type: "POST",
                    url: "/agregar_respuesta_encuesta",
                    data: {
                        id_encu: encuId,
                        respuesta: resp,
                        id_usuario: form.find('.txtUsuario').val(),
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                    },
                    success: function (data) {
                        var newComment = `
                        <article class="respuesta p-6 text-base bg-white rounded-lg dark:bg-gray-900 m-2" style="background-color: rgb(48, 47, 47); color: white;">
                            <footer class="flex justify-between items-center mb-2">
                                <div class="flex items-center">
                                    <p class="inline-flex items-center mr-3 text-sm font-semibold">
                                        <img class="mr-2 w-6 h-6 rounded-full" src="${ruta_imagen}">
                                        ${nombre}
                                    </p>
                                </div>
                            </footer>
                            <p>${resp}</p>
                            <div class="flex items-center mt-4 space-x-4">
                            </div>
                        </article>
                    `;

                        var encuList = $("#encuList-" + encuId);
                        encuList.append(newComment);

                        form.find(".charCountRespuesta").text("0 / 150");

                        form.find(".respuesta").val("");

                        // Mostrar una notificación SweetAlert en caso de éxito
                        Swal.fire({
                            title: '¡Éxito!',
                            text: 'Tu respuesta se ha enviado correctamente.',
                            icon: 'success',
                            confirmButtonText: 'Aceptar'
                        });
                    },
                    error: function (data) {
                        // Mostrar una notificación SweetAlert en caso de error
                        Swal.fire({
                            title: 'Error',
                            text: 'Hubo un problema al enviar tu respuesta.',
                            icon: 'error',
                            confirmButtonText: 'Aceptar'
                        });
                    }
                });
            }
        });
    });
});

// Obtén todos los elementos con la clase publi_descripcion
var elementosConClase = document.getElementsByClassName('descripcion');

// Expresión regular para encontrar enlaces en el texto
var regexEnlace = /(https?:\/\/[^\s]+)/g;

// Itera sobre cada elemento con la clase y aplica la transformación
for (var i = 0; i < elementosConClase.length; i++) {
    var elemento = elementosConClase[i];
    var texto = elemento.innerText;

    // Reemplaza los enlaces con etiquetas de enlace y el texto del dominio
    var textoConEnlaces = texto.replace(regexEnlace, function (enlace) {
        // Extraer el dominio del enlace
        var dominio = new URL(enlace).hostname;

        // Crear el enlace con el dominio como texto
        return '<a href="' + enlace + '" target="_blank" style="color: blue">' + dominio + '</a>';
    });

    // Actualiza el contenido del elemento con enlaces
    elemento.innerHTML = textoConEnlaces;
}


// Espera a que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function () {
    // Función para aplicar el filtro
    function aplicarFiltro(texto) {
        document.querySelectorAll(".publicacion").forEach(elemento => {
            elemento.innerText.toLowerCase().includes(texto.toLowerCase())
                ? elemento.classList.remove("hidden")
                : elemento.classList.add("hidden");
        });
    }

    // Agrega un evento de clic al contenedor de botones
    document.querySelector(".publiacion-card").addEventListener("click", function (event) {
        // Verifica si el elemento clicado es un botón con la clase 'sede-boton'
        if (event.target.classList.contains("sede-boton")) {
            // Obtén el valor del select
            var textoBoton = document.querySelector("#filtroSede").value.trim();

            // Actualiza el valor del input con el valor del botón
            document.getElementById("buscador").value = textoBoton;

            // Aplica el filtro
            aplicarFiltro(textoBoton);
        }
    });

    // Agrega un evento de cambio al select
    document.querySelector("#filtroSede").addEventListener("change", function (event) {
        // Obtén el valor del select
        var textoBoton = event.target.value.trim();

        // Actualiza el valor del input con el valor del select
        document.getElementById("buscador").value = textoBoton;

        // Aplica el filtro
        aplicarFiltro(textoBoton);
    });

    // Agrega un evento de tecla al documento
    document.addEventListener("keyup", e => {
        if (e.target.matches("#buscador")) {
            // Aplica el filtro
            aplicarFiltro(e.target.value);
        }
    });
});