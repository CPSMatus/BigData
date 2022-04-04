


const X_INTERVAL = ["0-10",
                  "10-20",
                  "20-30",
                  "30-40",
                  "40-45",

                  "45-50",
                  "50-60",
                  "60-70",
                  "70-80",
                  "80-90"];

const X_INTERVAL_JORNADAS = ["J01",
                  "J02",
                  "J03",
                  "J04",
                  "J05",

                  "J06",
                  "J07",
                  "J08",
                  "J09",
                  "J10",
                  "J11",
                  "J12",
                  "J13",
                  "J14",
                  "J15",
                  "J16",
                  "J17"];


async function retrieve_jornada_info(){
  var url = new URL('https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/ultima_jornada');
  const response = await fetch(url);
  var datapoints = await response.json();

  return datapoints;
}

retrieve_jornada_info().then(datapoints =>{
  var jornada = datapoints.items[0];
  var id_jornada = jornada.jornada_id;

  var time_and_date_array = jornada['fecha'].split('T');

  var arbitro = ( jornada['nombre_arbitraje'] ) + " " + ( jornada['apellido_arbitraje'] );
  //Split fecha y hora

  fecha = document.getElementById("fecha").innerHTML = time_and_date_array[0];

  var time_array = time_and_date_array[1].split(':');

  hora = document.getElementById("hora").innerHTML = time_array[0] + ':' + time_array[1];

  abitraje = document.getElementById("arbitraje").innerHTML = "Arbitró: " + arbitro;

  const image_local = document.getElementById("image_local");
  const image_visitante = document.getElementById("image_visitante");

  if (jornada['is_local'] == 1){

    image_visitante.src = jornada['logo_equipo'];
  }else {

    image_local.src = jornada['logo_equipo'];

  }






  console.log(id_jornada);
  retrieve_golstats_general_info(id_jornada);

  retrieve_distance_team(id_jornada);
  retrieve_sprints_team(id_jornada);

  golstats_handler(id_jornada);

});




function retrieve_golstats_general_info(id_jornada){
  var url = new URL('https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/golstats/general_golstats');

  var params = { id_jornada:id_jornada }; // or:

  url.search = new URLSearchParams(params).toString();

  const golstats_general_response = fetch(url);

  golstats_general_response.then((response) =>{

  return response.json();

  }).then((items) => {
    const data = items.items[0];

    amarillas = document.getElementById("total_amarillas").innerHTML = "Total: " + data['tarjetas_amarillas'];

    rojas = document.getElementById("total_rojas").innerHTML = "Total: " +  data['tarjetas_rojas'];


  });
}



 function golstats_handler(id_jornada){
   //Obtener la informacion de mi id_equipo

  var url = new URL('https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/general/mi_equipo');
  const my_team_info_fetch = fetch(url);
  my_team_info_fetch.then((response) =>{

  return response.json();

  }).then((items) => {
   const my_team_response = items.items[0];
   var my_team_id = my_team_response['equipo_id'];



   //Crear el escucha del checkbox para mostrar informacion del equipo rival


     //Obtener la informacion de Golstats x default de mi Equipo
    retrieve_golstats_team_defensiva(id_jornada,my_team_id);
    retrieve_golstats_team_ofensiva(id_jornada,my_team_id);
  });



}



function retrieve_golstats_team_ofensiva(id_jornada,my_team_id){
  var url = new URL('https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/golstats/ofensiva_golstats');

  var params = { id_jornada:id_jornada,
                id_equipo:my_team_id  }; // or:

  url.search = new URLSearchParams(params).toString();

  const response_distance = fetch(url);

  response_distance.then((response) =>{

  return response.json();

  }).then((items) => {
    const data_ofensiva = items.items[0];
    console.log("GOLSTATS OFENSIVA: ");
    console.log(data_ofensiva)
    var result_ofensiva = []
  //  result_ofensiva.push(data_ofensiva['faltas_recibidas']);
  //  result_ofensiva.push(data_ofensiva['goles']);
    result_ofensiva.push(data_ofensiva['pases_acertados_cancha_propia']);
    result_ofensiva.push(data_ofensiva['pases_acertados_cancha_rival']);
    result_ofensiva.push(data_ofensiva['pases_no_acertados_cancha_propia']);
    result_ofensiva.push(data_ofensiva['pases_no_acertados_cancha_rival']);
    result_ofensiva.push(data_ofensiva['uno_vs_uno_exitoso_ofensivo']);
    result_ofensiva.push(data_ofensiva['uno_vs_uno_no_exitoso_ofensivo']);


    //console.log(result_ofensiva);
    draw_chart_ofensiva_golstats(result_ofensiva);
  });
}


function draw_chart_ofensiva_golstats(result) {
  var ofensiva_canvas = document.getElementById('ofensiva-chart');

  const ofensiva_data = {
    labels: [
      'pases acertados cancha propia',
      'pases acertados cancha rival',
      'pases no acertados cancha propia',
      'pases no acertados cancha rival',
    //  'goles permitidos',
    //  'faltas recibidas',
      '1 vs 1 exitoso ofensivo',
      '1 vs 1 no exitoso ofensivo'
    ],
    datasets: [{
      label: 'Equipo Local',
      data: result,
      fill: true,
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgb(255, 99, 132)',
      pointBackgroundColor: 'rgb(255, 99, 132)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgb(255, 99, 132)'
    } ]
  };


  var radarChart_defensiva = new Chart(ofensiva_canvas, {
    type: 'radar',
    data: ofensiva_data,
    options:{
        responsive: true,
        maintainAspectRatio: false
    }
  });

}







function retrieve_golstats_team_defensiva(id_jornada,my_team_id){
  var url = new URL('https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/golstats/defensiva_golstats');

  var params = { id_jornada:id_jornada,
                id_equipo:my_team_id  }; // or:

  url.search = new URLSearchParams(params).toString();

  const response_distance = fetch(url);

  response_distance.then((response) =>{

  return response.json();

  }).then((items) => {
    const data_defensiva = items.items[0];
    console.log("GOLSTATS DEFENSIVA: ");
    console.log(data_defensiva)
    var result_defensiva = []
    result_defensiva.push(data_defensiva['balones_recuperados_disputa']);
    result_defensiva.push(data_defensiva['rechaces']);
    //result_defensiva.push(data_defensiva['goles_permitidos']);
    result_defensiva.push(data_defensiva['tiros_a_gol_recibidos']);
    //result_defensiva.push(data_defensiva['faltas_cometidas']);
    result_defensiva.push(data_defensiva['uno_vs_uno_exitoso_defensivo']);
    result_defensiva.push(data_defensiva['uno_vs_uno_no_exitoso_defensivo']);


  //  console.log(result_defensiva);
    draw_chart_defensiva_golstats(result_defensiva);

  });
}


function draw_chart_defensiva_golstats(result) {
  var defensiva_canvas = document.getElementById('defensiva-chart');

  const defensiva_data = {
    labels: [
      'balones recuperados en disputa',
      'rechaces',
    //  'goles permitidos',
      'tiros a gol recibidos',
    //  'faltas cometidas',
      '1 vs 1 exitoso defensivo',
      '1 vs 1 no exitoso defensivo'
    ],
    datasets: [{
      label: 'Equipo Local',
      data: result,
      fill: true,
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgb(255, 99, 132)',
      pointBackgroundColor: 'rgb(255, 99, 132)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgb(255, 99, 132)'
    } ]
  };


  var radarChart_defensiva = new Chart(defensiva_canvas, {
    type: 'radar',
    data: defensiva_data,
    options:{
        responsive: true,
        maintainAspectRatio: false
    }
  });

}








function retrieve_sprints_team(id_jornada){
  var url = new URL('https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/wimu/wimu_sprints_team');

  var params = { id_jornada:id_jornada}; // or:

  url.search = new URLSearchParams(params).toString();

  const response_sprints = fetch(url);

  response_sprints.then((response) =>{

  return response.json();

  }).then((items) => {
    const sprints_data = items.items[0];

    var result = []
    for(var i in sprints_data){
      result.push(sprints_data[i]);
    }
    console.log(result);

    draw_sprints_chart(result);
  });
}

function draw_sprints_chart(result) {
var canvas_sprint = document.getElementById('sprints-chart').getContext('2d');
  var my_sprint_chart = new Chart(canvas_sprint, {
      type: 'line',
      data: {
          labels: X_INTERVAL,
          datasets: [{

              data: result, //retrieve de data from the api
              backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 159, 64, 0.2)'
              ],
              borderColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(255, 159, 64, 1)'
              ],
              borderWidth: 1
          }]
      },
      options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
              y: {
                  beginAtZero: true
              }
          }
      }
  });
}




function retrieve_distance_team(id_jornada){
  var url = new URL('https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/wimu/wimu_distance_team');

  var params = { id_jornada:id_jornada}; // or:

  url.search = new URLSearchParams(params).toString();

  const response_distance = fetch(url);

  response_distance.then((response) =>{

  return response.json();

  }).then((items) => {
    const data_distance = items.items[0];

    var result = []
    for(var i in data_distance){
      result.push(data_distance[i]);
    }
    console.log(result);

    draw_chart_distance(result);
  });
}


function draw_chart_distance(result) {
var distance_canvas = document.getElementById('distance-chart').getContext('2d');
  var team_distance_chart = new Chart(distance_canvas, {
      type: 'line',
      data: {
          labels: X_INTERVAL,
          datasets: [{

              data: result, //retrieve de data from the api
              backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 159, 64, 0.2)'
              ],
              borderColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(255, 159, 64, 1)'
              ],
              borderWidth: 1
          }]
      },
      options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
              y: {
                  beginAtZero: true
              }
          }
      }
  });
}
