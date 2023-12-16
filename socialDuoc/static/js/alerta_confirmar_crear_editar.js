function crear(id) {
    Swal.fire({
    title: "¿Estás seguro?",
    text: "Esta acción debera esperar la aprobacion de un superior.",
    icon: "question",
    showCancelButton: true,
    confirmButtonText: "Sí, estoy seguro",
    cancelButtonText: "Cancelar",
}).then((result) => {
        if (result.isConfirmed) {
            // Encuentra el formulario padre del botón por su clase y lo envía
            var button = document.querySelector('.formulario'); // Reemplaza 'tu_clase_de_boton' con la clase de tu botón
            var form = button.closest('form');
            if (form) {
                form.submit();
            }
        }
    });
}

function editar(id) {
    Swal.fire({
        title: '¿Deseas editar este elemento?',
        text: 'Por favor, confirma si deseas editar este elemento.',
        icon: 'question',
        showCancelButton: true,
        confirmButtonText: 'Editar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            // Encuentra el formulario padre del botón por su clase y lo envía
            var button = document.querySelector('.formulario'); // Reemplaza 'tu_clase_de_boton' con la clase de tu botón
            var form = button.closest('form');
            if (form) {
                form.submit();
            }
        }
    });
}


// Obtener las referencias de los elementos de fecha
const fechaI = document.getElementById("fechaI");
const fechaF = document.getElementById("fechaF");

// Obtener la fecha de hoy
const fechaHoy = new Date();
fechaHoy.setHours(0, 0, 0, 0); // Establecer la hora a 00:00:00.000

// Restar un día a la fecha de hoy
fechaHoy.setDate(fechaHoy.getDate() - 1);

// Agregar un evento de escucha para la validación
fechaI.addEventListener("input", validarFechas);
fechaF.addEventListener("input", validarFechas);

function validarFechas() {
    const fechaInicio = new Date(fechaI.value);
    const fechaFin = new Date(fechaF.value);

    if (fechaInicio < fechaHoy) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'La fecha de inicio debe ser igual o mayor a la fecha de hoy menos un día.',
        });
        fechaI.value = ""; // Limpiar el campo de fecha de inicio
    }

    if (fechaFin < fechaHoy) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: 'La fecha de fin debe ser igual o mayor a la fecha de hoy menos un día.',
        });
        fechaF.value = ""; // Limpiar el campo de fecha de fin
    }
}