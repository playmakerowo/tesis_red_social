document.addEventListener('DOMContentLoaded', function() {
    // Función para actualizar el contador de caracteres
    function updateCharCount() {
        const comentarioInputs = document.querySelectorAll('.txtRespuesta');
        const charCountElements = document.querySelectorAll('.charCountRespuesta');
        const maxChars = 150; // Cambia esto al número máximo de caracteres permitidos

        comentarioInputs.forEach((comentarioInput, index) => {
            if (comentarioInput && comentarioInput.value !== undefined) {
                const currentLength = comentarioInput.value.length;
                if (charCountElements[index]) {
                    charCountElements[index].textContent = `${currentLength} / ${maxChars}`;
                }
            }
        });
    }

    // Agrega un evento 'input' para actualizar el contador en tiempo real
    const comentarioInputs = document.querySelectorAll('.txtRespuesta');
    comentarioInputs.forEach(comentarioInput => {
        comentarioInput.addEventListener('input', updateCharCount);
    });

    // Llama a la función para establecer los contadores iniciales
    updateCharCount();
});