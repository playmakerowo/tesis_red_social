document.addEventListener("keyup", e => {

    if (e.target.matches("#buscador")) {

        document.querySelectorAll(".item").forEach(elemento => {
            elemento.innerText.toLowerCase().includes(e.target.value.toLowerCase())
                ? elemento.classList.remove("hidden")
                : elemento.classList.add("hidden");
        });

    }

})

$(document).ready(function () {
    // Manejador para todos los formularios con la clase "comentForm"
    $('#agregar').on('submit', function (e) {
        e.preventDefault();
        var form = $(this);
        var id_usuario = $('#select_usuarios').val();
        var id_seccion = $('#id_seccion').val();
        // Realiza una solicitud AJAX para agregar el comentario
        $.ajax({
            type: "POST",
            url: "/agregar_usuario_seccion",
            data: {
                id_usuario: id_usuario,
                id_seccion: id_seccion,
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {
                console.log(data);
                if (data.success === 'EXITO') {
                    var usuarios_registrados = data.usuarios_registrados; // Obtén la lista de usuarios actualizada

                    // Encuentra la lista de usuarios de la sección específica
                    var userList = $("#userList");  // Asegúrate de tener un elemento con el id "userList"
                    // Encuentra el usuario seleccionado en el dropdown
                    var selectedOption = $('#select_usuarios option:selected');

                    // Oculta el usuario seleccionado en la lista de usuarios
                    var selectedUserId = selectedOption.val();
                    selectedOption.remove();
                    // Limpia la sección de usuarios
                    userList.empty();
                    // Limpia y actualiza el select
                    form.find("#select_usuarios")
                        .val("Selecciona un usuario");

                    // Agrega los nuevos comentarios a la lista de comentarios específica
                    usuarios_registrados.forEach(function (usuario_registrado) {
                        var newUsuario = `
                        <li class="flex item py-2 justify-between relative w-full hover:bg-gray-800 rounded">
                            <a href="/perfil_usuarios/${usuario_registrado.id_usuario}">
                            <div class="flex items-center p-2 cursor-pointer">
                                ${usuario_registrado.foto == '0' ?
                                `<img class="h-10 w-10 rounded-full" src="/static/img/user.jpg">` :
                                `<img class="h-10 w-10 rounded-full" src="data:image/png;base64, ${usuario_registrado.foto}">`
                            }
                                <div class="ml-2 overflow-hidden">
                                    <p class="text-sm font-medium text-slate-900">${usuario_registrado.nombre}</p>
                                    <p class="text-sm text-slate-500 truncate correo-hidden">${usuario_registrado.correo}</p>
                                </div>
                            </div>
                            </a>
                            <form action="" class="eliminar" id="eliminar_${usuario_registrado.id_usuario}">
                                <input type="text" name="id_seccion" id="id_seccion" value="${id_seccion}" hidden>
                                <input type="text" name="id_usuario" id="id_usuario" value="${usuario_registrado.id_usuario}" hidden>
                                <button type="submit" name="accion" value="eliminar_${usuario_registrado.id_usuario}"
                                    class="text-white bg-red-600 rounded-lg px-2 m-2 p-2 hover:bg-red-900">
                                    <i class="fa fa-trash fa-lg" aria-hidden="true"></i>
                                </button>
                            </form>
                        </li>
                    `;
                        userList.append(newUsuario);
                    });
                    


                    form.find("#select_usuarios").val("");
                    Swal.fire({
                        icon: 'success',
                        title: 'Exito',
                        text: 'Usuario agregado',
                    });
                }
            },
            error: function (response, status, error) {
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: 'Hubo un error al procesar la solicitud. Detalles: ' + error,
                });
            }
        });
    });
});

$(document).on('submit', '.eliminar', function (e) {
    e.preventDefault();
    var form = $(this);
    var id_usuario = form.find('input[name="id_usuario"]').val();
    var id_seccion = form.find('input[name="id_seccion"]').val();

    // Utilizamos SweetAlert para mostrar un mensaje de confirmación
    Swal.fire({
        title: '¿Estás seguro?',
        text: 'Esta acción eliminará al usuario de la seccion. Perdera acceso al grupo del chat.',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, eliminarlo',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            // Realiza una solicitud AJAX para eliminar el usuario
            $.ajax({
                type: "POST",
                url: "/eliminar_usuario_seccion",
                data: {
                    id_usuario: id_usuario,
                    id_seccion: id_seccion,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                },
                success: function (data) {
                    form.closest('li').hide();
                    console.log(data);
                    if (data.success === 'EXITO') {
                        Swal.fire({
                            icon: 'success',
                            title: 'Éxito',
                            text: 'Usuario eliminado',
                        });
                    }
                },
                error: function (response, status, error) {
                    Swal.fire({
                        icon: 'error',
                        title: 'Error',
                        text: 'Hubo un error al procesar la solicitud. Detalles: ' + error,
                    });
                }
            });
        }
    });
});