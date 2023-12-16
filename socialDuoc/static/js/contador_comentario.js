document.body.addEventListener('input', function (event) {
  if (event.target && event.target.classList.contains('txtComentario')) {
      updateCharCount();
  }
});

// Función para actualizar el contador de caracteres
function updateCharCount() {
  const comentarioInputs = document.querySelectorAll('.txtComentario');
  const charCountElements = document.querySelectorAll('.charCountPregunta');
  const maxChars = 500; // Cambia esto al número máximo de caracteres permitidos

  comentarioInputs.forEach((comentarioInput, index) => {
      const currentLength = comentarioInput.value.length;
      if (charCountElements[index]) {
          charCountElements[index].textContent = `${currentLength} / ${maxChars}`;
      }
  });
}

// Llama a la función para establecer los contadores iniciales
updateCharCount();