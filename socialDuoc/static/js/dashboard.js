// ################################################################################
// ################################################################################
// ##################################PUBLICACION###################################
// ################################################################################
// ################################################################################
var publiUltimaSemana = publicacionesUltimaSemanaData;
// Obtén las listas de la ultimaa semana y número de publicaciones
var Fecha = publiUltimaSemana.map((publiUltimaSemana) => publiUltimaSemana["Fecha"]);


window.addEventListener("load", function () {
  // Obtén los datos de los días y número de publicaciones
  const Dias = publiUltimaSemana.map((publiUltimaSemana) => publiUltimaSemana["Dia"]); // Debes proporcionar tus propios datos aquí
  const NumeroPublicaciones = publiUltimaSemana.map((publiUltimaSemana) => publiUltimaSemana["NúmeroPublicaciones"]); // Debes proporcionar tus propios datos aquí

  const options = {
    colors: ["#1A56DB"], // Color de las barras
    series: [
      {
        name: "Número de Publicaciones",
        data: NumeroPublicaciones,
      },
    ],
    chart: {
      type: "bar",
      height: "320px",
      fontFamily: "Inter, sans-serif",
      toolbar: {
        show: false,
      },
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: "70%",
        borderRadius: 8,
      },
    },
    xaxis: {
      categories: Dias, // Etiquetas del eje X
      labels: {
        style: {
          fontFamily: "Inter, sans-serif",
          fontSize: "12px", // Tamaño de fuente de las etiquetas
        },
      },
    },
    yaxis: {
      title: {
        text: "Número de Publicaciones", // Título del eje Y
        style: {
          fontFamily: "Inter, sans-serif",
        },
      },
    },
    dataLabels: {
      enabled: false,
    },
    legend: {
      show: false,
    },
    fill: {
      opacity: 1,
    },
  };

  if (document.getElementById("column-chart") && typeof ApexCharts !== "undefined") {
    const chart = new ApexCharts(document.getElementById("column-chart"), options);
    chart.render();
  }
});


// ################################################################################
// ################################################################################
// ##################################ENCUESTAS#####################################
// ################################################################################
// ################################################################################
var encuUltimaSemana = encuestasUltimaSemanaData;
// Obtén las listas de la ultimaa semana y número de publicaciones
var FechaE = encuUltimaSemana.map((encuUltimaSemana) => encuUltimaSemana["Fecha"]);

window.addEventListener("load", function () {
  // Obtén los datos de los días y número de publicaciones
  const Dias = encuUltimaSemana.map((encuUltimaSemana) => encuUltimaSemana["Dia"]);
  const NumeroEncuestas = encuUltimaSemana.map((encuUltimaSemana) => encuUltimaSemana["NúmeroEncuestas"]);

  const options = {
    colors: ["#68A458"], // Color de las barras
    series: [
      {
        name: "Número de Encuestas",
        data: NumeroEncuestas,
      },
    ],
    chart: {
      type: "bar",
      height: "320px",
      fontFamily: "Inter, sans-serif",
      toolbar: {
        show: false,
      },
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: "70%",
        borderRadius: 8,
      },
    },
    xaxis: {
      categories: Dias, // Etiquetas del eje X
      labels: {
        style: {
          fontFamily: "Inter, sans-serif",
          fontSize: "12px", // Tamaño de fuente de las etiquetas
        },
      },
    },
    yaxis: {
      title: {
        text: "Número de Encuestas", // Título del eje Y
        style: {
          fontFamily: "Inter, sans-serif",
        },
      },
    },
    dataLabels: {
      enabled: false,
    },
    legend: {
      show: false,
    },
    fill: {
      opacity: 1,
    },
  };

  if (document.getElementById("column-chart-2") && typeof ApexCharts !== "undefined") {
    const chart = new ApexCharts(document.getElementById("column-chart-2"), options);
    chart.render();
  }
});

// ################################################################################
// ################################################################################
// ###################################EVENTO#######################################
// ################################################################################
// ################################################################################

var eveUltimaSemana = eventosUltimaSemanaData;
// Obtén las listas de la ultimaa semana y número de publicaciones
var FechaEv = eveUltimaSemana.map((eveUltimaSemana) => eveUltimaSemana["Fecha"]);

window.addEventListener("load", function () {
  // Obtén los datos de los días y número de publicaciones
  const Dias = eveUltimaSemana.map((eveUltimaSemana) => eveUltimaSemana["Dia"]);
  const NumeroEventos = eveUltimaSemana.map((eveUltimaSemana) => eveUltimaSemana["NúmeroEventos"]);

  const options = {
    colors: ["#CD0D87"], // Color de las barras
    series: [
      {
        name: "Número de Eventos",
        data: NumeroEventos,
      },
    ],
    chart: {
      type: "bar",
      height: "320px",
      fontFamily: "Inter, sans-serif",
      toolbar: {
        show: false,
      },
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: "70%",
        borderRadius: 8,
      },
    },
    xaxis: {
      categories: Dias, // Etiquetas del eje X
      labels: {
        style: {
          fontFamily: "Inter, sans-serif",
          fontSize: "12px", // Tamaño de fuente de las etiquetas
        },
      },
    },
    yaxis: {
      title: {
        text: "Número de Eventos", // Título del eje Y
        style: {
          fontFamily: "Inter, sans-serif",
        },
      },
    },
    dataLabels: {
      enabled: false,
    },
    legend: {
      show: false,
    },
    fill: {
      opacity: 1,
    },
  };

  if (document.getElementById("column-chart-3") && typeof ApexCharts !== "undefined") {
    const chart = new ApexCharts(document.getElementById("column-chart-3"), options);
    chart.render();
  }
});




// ################################################################################
// ################################################################################
// #############################GRAFICOS DE LINEA##################################
// ################################################################################
// ################################################################################

// ################################PUBLICACION#####################################
var publiSemana = publicacionesSemanaData;

// Obtén las listas de inicio de la semana, fin de la semana y número de publicaciones
var inicioSemana = publiSemana.map((publiSemana) => publiSemana["InicioSemana"]);
var finSemana = publiSemana.map((publiSemana) => publiSemana["FinSemana"]);
var numeroPublicaciones = publiSemana.map((publiSemana) => publiSemana["NúmeroPublicaciones"]);
// Crear una lista de etiquetas para el eje x que muestre el rango de días
var etiquetasEjeX = inicioSemana.map((inicio, index) => inicio + ' - ' + finSemana[index]);


//grafico linea
// ApexCharts options and config
window.addEventListener("load", function () {
  let options = {
    chart: {
      height: "100%",
      maxWidth: "100%",
      type: "area",
      fontFamily: "Inter, sans-serif",
      dropShadow: {
        enabled: false,
      },
      toolbar: {
        show: false,
      },
    },
    tooltip: {
      enabled: true,
      x: {
        show: false,
      },
    },
    fill: {
      type: "gradient",
      gradient: {
        opacityFrom: 0.55,
        opacityTo: 0,
        shade: "#FAD501",
        gradientToColors: ["#1C64F2"],
      },
    },
    dataLabels: {
      enabled: false,
    },
    stroke: {
      width: 6,
    },
    grid: {
      show: false,
      strokeDashArray: 4,
      padding: {
        left: 2,
        right: 2,
        top: 0
      },
    },
    series: [
      {
        name: "Número de Publicaciones en semanas",
        data: numeroPublicaciones, // Usar la lista de números de publicaciones
        color: "#1A56DB",
      },
    ],
    xaxis: {
      categories: etiquetasEjeX, // Usar la lista de inicio de la semana como etiquetas del eje x
      labels: {
        show: true, // Mostrar las etiquetas en el eje x
      },
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: true, // Mostrar las marcas del eje x
      },
    },
    yaxis: {
      show: true, // Mostrar el eje y
      title: {
        text: "Número de Publicaciones", // Título del eje y
      },
    },
  };

  if (document.getElementById("area-chart") && typeof ApexCharts !== 'undefined') {
    const chart = new ApexCharts(document.getElementById("area-chart"), options);
    chart.render();
  }
});

// ################################ENCUESTA#####################################
var encuSemana = encuestasSemanaData;

// Obtén las listas de inicio de la semana, fin de la semana y número de publicaciones
var inicioSemana = encuSemana.map((encuSemana) => encuSemana["InicioSemana"]);
var finSemana = encuSemana.map((encuSemana) => encuSemana["FinSemana"]);
var NumeroEncuestas = encuSemana.map((encuSemana) => encuSemana["NúmeroEncuestas"]);
// Crear una lista de etiquetas para el eje x que muestre el rango de días
var etiquetasEjeX = inicioSemana.map((inicio, index) => inicio + ' - ' + finSemana[index]);


//grafico linea
// ApexCharts options and config
window.addEventListener("load", function () {
  let options = {
    chart: {
      height: "100%",
      maxWidth: "100%",
      type: "area",
      fontFamily: "Inter, sans-serif",
      dropShadow: {
        enabled: false,
      },
      toolbar: {
        show: false,
      },
    },
    tooltip: {
      enabled: true,
      x: {
        show: false,
      },
    },
    fill: {
      type: "gradient",
      gradient: {
        opacityFrom: 0.55,
        opacityTo: 0,
        shade: "#68A458",
        gradientToColors: ["#68A458"],
      },
    },
    dataLabels: {
      enabled: false,
    },
    stroke: {
      width: 6,
    },
    grid: {
      show: false,
      strokeDashArray: 4,
      padding: {
        left: 2,
        right: 2,
        top: 0
      },
    },
    series: [
      {
        name: "Número de Encuestas en semanas",
        data: NumeroEncuestas, // Usar la lista de números de publicaciones
        color: "#68A458",
      },
    ],
    xaxis: {
      categories: etiquetasEjeX, // Usar la lista de inicio de la semana como etiquetas del eje x
      labels: {
        show: true, // Mostrar las etiquetas en el eje x
      },
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: true, // Mostrar las marcas del eje x
      },
    },
    yaxis: {
      show: true, // Mostrar el eje y
      title: {
        text: "Número de Encuestas", // Título del eje y
      },
    },
  };

  if (document.getElementById("area-chart-2") && typeof ApexCharts !== 'undefined') {
    const chart = new ApexCharts(document.getElementById("area-chart-2"), options);
    chart.render();
  }
});

// ################################EVENTO##########################################
var eveSemana = eventosSemanaData;

// Obtén las listas de inicio de la semana, fin de la semana y número de publicaciones
var inicioSemana = eveSemana.map((eveSemana) => eveSemana["InicioSemana"]);
var finSemana = eveSemana.map((eveSemana) => eveSemana["FinSemana"]);
var NumeroEventos = eveSemana.map((eveSemana) => eveSemana["NúmeroEventos"]);
// Crear una lista de etiquetas para el eje x que muestre el rango de días
var etiquetasEjeX = inicioSemana.map((inicio, index) => inicio + ' - ' + finSemana[index]);



//grafico linea
// ApexCharts options and config
window.addEventListener("load", function () {
  let options = {
    chart: {
      height: "100%",
      maxWidth: "100%",
      type: "area",
      fontFamily: "Inter, sans-serif",
      dropShadow: {
        enabled: false,
      },
      toolbar: {
        show: false,
      },
    },
    tooltip: {
      enabled: true,
      x: {
        show: false,
      },
    },
    fill: {
      type: "gradient",
      gradient: {
        opacityFrom: 0.55,
        opacityTo: 0,
        shade: "#CD0D87",
        gradientToColors: ["#CD0D87"],
      },
    },
    dataLabels: {
      enabled: false,
    },
    stroke: {
      width: 6,
    },
    grid: {
      show: false,
      strokeDashArray: 4,
      padding: {
        left: 2,
        right: 2,
        top: 0
      },
    },
    series: [
      {
        name: "Número de Eventos en semanas",
        data: NumeroEventos, // Usar la lista de números de publicaciones
        color: "#CD0D87",
      },
    ],
    xaxis: {
      categories: etiquetasEjeX, // Usar la lista de inicio de la semana como etiquetas del eje x
      labels: {
        show: true, // Mostrar las etiquetas en el eje x
      },
      axisBorder: {
        show: false,
      },
      axisTicks: {
        show: true, // Mostrar las marcas del eje x
      },
    },
    yaxis: {
      show: true, // Mostrar el eje y
      title: {
        text: "Número de Eventos", // Título del eje y
      },
    },
  };

  if (document.getElementById("area-chart-3") && typeof ApexCharts !== 'undefined') {
    const chart = new ApexCharts(document.getElementById("area-chart-3"), options);
    chart.render();
  }
});


// ################################################################################
// ################################################################################
// ################################################################################
// ################################################################################
// ################################################################################


var carrerasAgrupadas = [];
var otrosCount = 0;

for (var i = 0; i < carrerasData.length; i++) {
  var carrera = carrerasData[i];

  // Si la carrera tiene menos de 5 alumnos, agrégala a la categoría "Otros"
  if (carrera.count < 3) {
    otrosCount += carrera.count; // Acumula la cantidad de alumnos en "Otros"
  } else {
    // Si la carrera tiene 5 o más alumnos, mantenla en el arreglo original
    carrerasAgrupadas.push(carrera);
  }
}

// Agrega la categoría "Otros" al arreglo si tiene al menos un alumno
if (otrosCount > 0) {
  carrerasAgrupadas.push({ nombre: "Otros", count: otrosCount });
}

// Crear arreglos para las series y etiquetas
const series = carrerasAgrupadas.map((carrerasAgrupadas) => carrerasAgrupadas.count);
const labels = carrerasAgrupadas.map((carrerasAgrupadas) => carrerasAgrupadas.nombre);
console.log(carrerasAgrupadas)

//grafico torta
window.addEventListener("load", function () {
  const getChartOptions = () => {
    return {
      series: series,
      colors: ["#1C64F2", "#16BDCA", "#03A636", "#7E4ADA", "#D791FB"],
      chart: {
        height: 420,
        width: "100%",
        type: "pie",
      },
      stroke: {
        colors: ["white"],
        lineCap: "",
      },
      plotOptions: {
        pie: {
          labels: {
            show: true,
          },
          size: "100%",
          dataLabels: {
            offset: -25
          }
        },
      },
      labels: labels,
      dataLabels: {
        enabled: true,
        style: {
          fontFamily: "Inter, sans-serif",
        },
      },
      legend: {
        position: "bottom",
        fontFamily: "Inter, sans-serif",
      },
      yaxis: {
        labels: {
          formatter: function (value) {
            return value + "%"
          },
        },
      },
      xaxis: {
        labels: {
          formatter: function (value) {
            return value + "%"
          },
        },
        axisTicks: {
          show: false,
        },
        axisBorder: {
          show: false,
        },
      },
    }
  }

  if (document.getElementById("pie-chart") && typeof ApexCharts !== 'undefined') {
    const chart = new ApexCharts(document.getElementById("pie-chart"), getChartOptions());
    chart.render();
  }
});