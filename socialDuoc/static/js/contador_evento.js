// Campo de entrada "Nombre del Evento"
const txtTitulo = document.getElementById('txtTitulo');
const charCountTitulo = document.getElementById('charCountTitulo');

// Campo de entrada "Descripcion del evento"
const txtDesc = document.getElementById('txtDesc');
const charCountDesc = document.getElementById('charCountDesc');

// Función para actualizar el contador de caracteres
function updateCharCount(inputElement, charCountElement, maxLength) {
    const currentLength = inputElement.value.length;
    charCountElement.textContent = `${currentLength} / ${maxLength}`;
}

// Actualiza los contadores de caracteres al cargar la página
updateCharCount(txtTitulo, charCountTitulo, 100);
updateCharCount(txtDesc, charCountDesc, 1500);

// Agrega eventos 'input' para actualizar los contadores en tiempo real
txtTitulo.addEventListener('input', function () {
    updateCharCount(txtTitulo, charCountTitulo, 100);
});

txtDesc.addEventListener('input', function () {
    updateCharCount(txtDesc, charCountDesc, 1500);
});
