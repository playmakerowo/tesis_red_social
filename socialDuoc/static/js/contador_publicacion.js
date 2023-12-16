const txtDesc = document.getElementById('txtDesc');
const charCountDesc = document.getElementById('charCountDesc');

txtDesc.addEventListener('input', function () {
    const currentLength = txtDesc.value.length;
    charCountDesc.textContent = `${currentLength} / 1500`;
});

function updateCharCount() {
    const currentLength = txtDesc.value.length;
    charCountDesc.textContent = `${currentLength} / 1500`;
}

// Llama a la función para inicializar el contador al cargar la página
updateCharCount();

// Agrega un evento 'input' para actualizar el contador en tiempo real
txtDesc.addEventListener('input', updateCharCount);