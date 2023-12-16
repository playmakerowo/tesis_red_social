document.addEventListener('DOMContentLoaded', function() {
    function updateCharCount() {
        const correoInputs = document.querySelectorAll('.txtCorreo');
        const charCountElements = document.querySelectorAll('.charCountRespuesta');
        const telefonoInput = document.getElementById('txtTelefono');
        const charCountTelefono = document.querySelector('.charCountTelefono');
        const maxChars0 = 50; // Cambia esto al número máximo de caracteres permitidos para el correo
        const maxChars = 9; // Cambia esto al número máximo de caracteres permitidos para el teléfono

        correoInputs.forEach((comentarioInput, index) => {
            if (comentarioInput && comentarioInput.value !== undefined) {
                const currentLength = comentarioInput.value.length;
                if (charCountElements[index]) {
                    charCountElements[index].textContent = `${currentLength} / ${maxChars0}`;
                }
            }
        });

        if (telefonoInput && telefonoInput.value !== undefined) {
            const currentLength = telefonoInput.value.length;
            if (charCountTelefono) {
                charCountTelefono.textContent = `${currentLength} / ${maxChars}`;
            }
        }
    }

    // Agrega un evento 'input' para actualizar el contador en tiempo real
    const correoInputs = document.querySelectorAll('.txtCorreo');
    const telefonoInput = document.getElementById('txtTelefono');
    correoInputs.forEach(comentarioInput => {
        comentarioInput.addEventListener('input', updateCharCount);
    });

    if (telefonoInput) {
        telefonoInput.addEventListener('input', updateCharCount);
    }

    // Llama a la función para establecer los contadores iniciales
    updateCharCount();
});