
// Campo de entrada "Nombre del Evento"
const txtTitulo = document.getElementById('txtTitulo');
const charCountTitulo = document.getElementById('charCountTitulo');

// Campo de entrada "Pregunta a realizar"
const txtPregunta = document.getElementById('txtPregunta');
const charCountPregunta = document.getElementById('charCountPregunta');

// Área de texto "Descripción del evento"
const txtDesc = document.getElementById('txtDesc');
const charCountDesc = document.getElementById('charCountDesc');

// Campo de entrada "Link (Opcional)"
const txtlink = document.getElementById('txtlink');
const charCountLink = document.getElementById('charCountLink');

function updateCharCount(inputElement, charCountElement, maxLength) {
    const currentLength = inputElement.value.length;
    charCountElement.textContent = `${currentLength} / ${maxLength}`;
}

// Inicializa los contadores con el valor inicial al cargar la página
updateCharCount(txtTitulo, charCountTitulo, 100);
updateCharCount(txtPregunta, charCountPregunta, 100);
updateCharCount(txtDesc, charCountDesc, 1500);
updateCharCount(txtlink, charCountLink, 150);

// Agrega eventos 'input' para actualizar los contadores en tiempo real
txtTitulo.addEventListener('input', function () {
    updateCharCount(txtTitulo, charCountTitulo, 100);
});

txtPregunta.addEventListener('input', function () {
    updateCharCount(txtPregunta, charCountPregunta, 100);
});

txtDesc.addEventListener('input', function () {
    updateCharCount(txtDesc, charCountDesc, 1500);
});

txtlink.addEventListener('input', function () {
    updateCharCount(txtlink, charCountLink, 150);
});

        