document.addEventListener("DOMContentLoaded", function () {
    var btnsRespuesta = document.querySelectorAll('.btnRespuesta');
    var btnEnviar = document.querySelectorAll('.btnEnviar');

    btnsRespuesta.forEach(function (btnRespuesta) {
        btnRespuesta.addEventListener('click', function () {
            var formId = btnRespuesta.getAttribute('data-form-id');
            var formulario = document.querySelector('[data-id="' + formId + '"] form.encuForm');
            var txtRespuesta = formulario.querySelector('[name="txtRespuesta"]');
            var respuesta = btnRespuesta.getAttribute('data-respuesta');

            // Actualizar el textarea con la respuesta del botón clicado
            txtRespuesta.value = respuesta;
        });
    });
});

let hideTimeout;

function showTooltip() {
    document.getElementsByClassName('perfil-pequeno').style.visibility = 'visible';
    document.getElementsByClassName('perfil-pequeno').style.opacity = '1';
}

function startHideTimeout() {
    hideTimeout = setTimeout(() => {
        document.getElementsByClassName('perfil-pequeno').style.visibility = 'hidden';
        document.getElementsByClassName('perfil-pequeno').style.opacity = '0';
    }, 2000); // 2000 milisegundos = 2 segundos
}

function clearHideTimeout() {
    clearTimeout(hideTimeout);
}