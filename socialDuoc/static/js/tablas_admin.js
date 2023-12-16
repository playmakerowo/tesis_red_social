//tabla de usuarios
$(document).ready(function () {
    $('#tabla_usuario').DataTable({
        responsive: true,
        autoWidth: false,
        dom: 'Bfrtip',
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json',
        },
        buttons: [
            {
                extend: 'colvis',
                columns: ':not(.noVis)'
            },
            {
                extend: 'excelHtml5',
                exportOptions: {
                    columns: ':visible'
                }
            },
            {
                extend: 'pdfHtml5',
                exportOptions: {
                    columns: ':visible'
                }
            }
        ],
        columnDefs: [
            { targets: [4], visible: false },  // Oculta la columna de comuna por defecto
            { responsivePriority: 1, targets: 1 },  // Nombre
            { responsivePriority: 2, targets: 6 },  // Acción
            { responsivePriority: 3, targets: 5 },  // Estado 
        ]
    });
});

//tabla de ENCUESTAS
$(document).ready(function () {
    $('#myTableencu').DataTable({
        responsive: true,
        autoWidth: false,
        dom: 'Bfrtip',
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json',
        },
        buttons: [
            {
                extend: 'colvis',
                columns: ':not(.noVis)'
            },
            {
                extend: 'excelHtml5',
                exportOptions: {
                    columns: ':visible'
                }
            },
            {
                extend: 'pdfHtml5',
                exportOptions: {
                    columns: ':visible'
                }
            }


        ],
        columnDefs: [
            { targets: [2], visible: false },// Oculta fecha de encuesta
            {'max-width': '320px', 'targets': 'titulo'}
        ]
        
    });
});


//tabla de publicaciones
$(document).ready(function () {
    $('#myTablepubli').DataTable({
        responsive: true,
        autoWidth: false,
        dom: 'Bfrtip',
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json',
        },
        buttons: [
            {
                extend: 'colvis',
                columns: ':not(.noVis)'
            },
            {
                extend: 'excelHtml5',
                exportOptions: {
                    columns: ':visible'
                }
            },
            {
                extend: 'pdfHtml5',
                exportOptions: {
                    columns: ':visible'
                }
            }
        ],
        columnDefs: [
            { targets: [2], visible: false },
            { targets: [4], visible: false },
          
        ]
    });
});


//tabla de busqueda de usuarios
$(document).ready(function () {
    $('#myTablebusqueda').DataTable({
        responsive: true,
        autoWidth: false,
        dom: 'Bfrtip',
        language: {
            url: '//cdn.datatables.net/plug-ins/1.13.7/i18n/es-ES.json',
        },
        buttons: [
            {
                extend: 'colvis',
                columns: ':not(.noVis)'
            }
            
        ],
        columnDefs: [
            { responsivePriority: 1, targets: 3 },  // Nombre
            { responsivePriority: 2, targets: 7 },  // Acción
        ]
    });
});