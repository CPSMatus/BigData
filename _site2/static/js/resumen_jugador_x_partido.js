
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


async function retrieve_jornada_info(){

  var url = new URL('https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/ultima_jornada');
  const response = await fetch(url);
  var datapoints = await response.json();

  return datapoints;
}

retrieve_jornada_info().then(datapoints =>{

  var jornada = datapoints.items[0];
  const  title  = document.getElementById("h_jornada").innerHTML = "   en Jornada " + " " + jornada['n_jornada'] ;


});


async function retrieve_player_info(){

  var  jugador_id = document.getElementById("jugador_jornada_id").innerHTML
  console.log(jugador_id);
  var url = new URL('https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/resumen/jugador_x_jornada');


  var params = { id_jugador_jornada:jugador_id}; // or:
  url.search = new URLSearchParams(params).toString();


  const response = await fetch(url);
  var datapoints = await response.json();

  return datapoints;
}


retrieve_player_info().then(datapoints =>{

    var jugador = datapoints.items[0];
    //Llenar la informacion de la plantilla con la informacion del jugador
    var jugar_nombre = to_lower_case(jugador['wimu_alias']);

    const player_photo = document.getElementById("player-photo");



    const  jugador_alias  = document.getElementById("span-card-1").innerHTML = jugar_nombre ;
    const jugador_title =  document.getElementById("h_jugador").innerHTML = "Analisis de " + jugar_nombre + " ";
    const  tiempo_juego = document.getElementById("tiempo_juego").innerHTML = jugador ['minutos_jugados'] + ' min' ;

    const  distancia_total = document.getElementById("distancia_total").innerHTML;

    const  entra = document.getElementById("entra").innerHTML = 'min ' + jugador['entra'] + "' ";

    const  sale = document.getElementById("sale").innerHTML = 'min '+ jugador['sale'] + "' " ;

    //player_photo.src(jugador['jugador_jornada_id']);
    player_photo.src = jugador['jugador_foto'];
    const posicion_jugador = jugador['id_posicion_principal'];
    console.log(jugador);
    const jugador_id = jugador['jugador_jornada_id'];
    retrieve_distance(jugador_id);
    retrieve_sprints(jugador_id);
    retrieve_hse(jugador_id);
    retrieve_position_data(posicion_jugador,jugador_id);

});

function to_lower_case(nombre){
  var nombre_array = nombre.split(' ');
  var first_letter = nombre_array[0].charAt(0);
  var second_letter = nombre_array[1].charAt(0);

  const pre_result1 = nombre_array[0].toLowerCase();
  const pre_result2 = nombre_array[1].toLowerCase();
  console.log(pre_result1);

  const index = 0; //Replace the first letter

  const result_1 =
  pre_result1.substring(0, index) +
  first_letter +
  pre_result1.substring(index + 1);

  const result_2 =
  pre_result2.substring(0, index) +
  second_letter +
  pre_result2.substring(index + 1);


  var final_result = result_1 + ' ' +  result_2
  return final_result;
}



function retrieve_position_data(posicion_jugador,id_jugador_jornada){
  var url = new URL('https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/golstats/posicion_golstats');

  var params = { id_jugador_jornada:id_jugador_jornada }; // or:

  url.search = new URLSearchParams(params).toString();

  const data_position_response = fetch(url);

  data_position_response.then((response) =>{

  return response.json();

  }).then((items) => {
    const data_position = items.items[0];
    position_array_data = create_array_per_position(posicion_jugador,data_position);
      console.log('POSICION:');
    console.log(position_array_data);

    draw_chart_position_golstats(position_array_data);
/*
    result_position_data.push(data_position['pacr']);
    result_position_data.push(data_position['pnacr']);
    result_position_data.push(data_position['brd']);
    result_position_data.push(data_position['bpd']);
    result_position_data.push(data_position['pacp']);
    result_position_data.push(data_position['pnacp']);
    result_position_data.push(data_position['uno_vs_uno_def_ex']);
    result_position_data.push(data_position['unos_vs_uno_def_nex']);
    result_position_data.push(data_position['uno_vs_uno_of_ex']);
    result_position_data.push(data_position['uno_vs_uno_of_nex']);
    result_position_data.push(data_position['bgap']);
    result_position_data.push(data_position['area_rival']);
    result_position_data.push(data_position['rechaces']);
    result_position_data.push(data_position['asistencias']);
    result_position_data.push(data_position['centros_izquierda']);
    result_position_data.push(data_position['centros_derecha']);
    result_position_data.push(data_position['tiro_gol']);
*/

  });
}


function create_array_per_position(position,data_position){
  var result_position_data = []

  if (position == 1){
    //Portero
  }

  if (position == 2){
    //Central
    result_position_data.push(data_position['pacr']);
    result_position_data.push(data_position['pnacr']);
    result_position_data.push(data_position['brd']);
    result_position_data.push(data_position['bpd']);
    result_position_data.push(data_position['pacp']);
    result_position_data.push(data_position['pnacp']);
    result_position_data.push(data_position['uno_vs_uno_def_ex']);
    result_position_data.push(data_position['unos_vs_uno_def_nex']);
    result_position_data.push(data_position['bgap']);
    result_position_data.push(data_position['area_rival']);
    result_position_data.push(data_position['rechaces']);

  }
  if (position == 3){
    //Carrilero
    result_position_data.push(data_position['pacr']);
    result_position_data.push(data_position['pnacr']);
    result_position_data.push(data_position['brd']);
    result_position_data.push(data_position['pacp']);
    result_position_data.push(data_position['pnacp']);
    result_position_data.push(data_position['uno_vs_uno_def_ex']);
    result_position_data.push(data_position['unos_vs_uno_def_nex']);
    result_position_data.push(data_position['uno_vs_uno_of_ex']);
    result_position_data.push(data_position['uno_vs_uno_of_nex']);
    result_position_data.push(data_position['bgap']);
    result_position_data.push(data_position['asistencias']);
    result_position_data.push(data_position['centros_izquierda']);
    result_position_data.push(data_position['centros_derecha']);
    result_position_data.push(data_position['tiro_gol']);


  }
  if (position == 4){
    //Volante
    result_position_data.push(data_position['pacr']);
    result_position_data.push(data_position['pnacr']);
    result_position_data.push(data_position['brd']);
    result_position_data.push(data_position['bpd']);
    result_position_data.push(data_position['uno_vs_uno_of_ex']);
    result_position_data.push(data_position['uno_vs_uno_of_nex']);
    result_position_data.push(data_position['area_rival']);
    result_position_data.push(data_position['asistencias']);
    result_position_data.push(data_position['centros_izquierda']);
    result_position_data.push(data_position['centros_derecha']);
    result_position_data.push(data_position['tiro_gol']);

  }
  if (position == 5){
    //Media punta
    result_position_data.push(data_position['pacr']);
    result_position_data.push(data_position['pnacr']);
    result_position_data.push(data_position['brd']);
    result_position_data.push(data_position['bpd']);
    result_position_data.push(data_position['uno_vs_uno_of_ex']);
    result_position_data.push(data_position['uno_vs_uno_of_nex']);
    result_position_data.push(data_position['area_rival']);
    result_position_data.push(data_position['asistencias']);
    result_position_data.push(data_position['centros_izquierda']);
    result_position_data.push(data_position['centros_derecha']);
    result_position_data.push(data_position['tiro_gol']);


  }
  if (position == 6){
    //Centro delantero
    result_position_data.push(data_position['pacr']);
    result_position_data.push(data_position['pnacr']);
    result_position_data.push(data_position['brd']);
    result_position_data.push(data_position['bpd']);
    result_position_data.push(data_position['uno_vs_uno_of_ex']);
    result_position_data.push(data_position['uno_vs_uno_of_nex']);
    result_position_data.push(data_position['area_rival']);
    result_position_data.push(data_position['asistencias']);
    result_position_data.push(data_position['tiro_gol']);

  }
  return result_position_data;
}


function retrieve_distance(id_jugador_jornada){
  var url = new URL('https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/wimu/distance_player');

  var params = { id_jugador_jornada:id_jugador_jornada }; // or:

  url.search = new URLSearchParams(params).toString();

  const distance_player_response = fetch(url);

  distance_player_response.then((response) =>{

  return response.json();

  }).then((items) => {
    const data_distance_player = items.items[0];

    var result_distance_player = []

    result_distance_player.push(data_distance_player['distance_0_10']);
    result_distance_player.push(data_distance_player['distance_10_20']);
    result_distance_player.push(data_distance_player['distance_20_30']);
    result_distance_player.push(data_distance_player['distance_30_40']);
    result_distance_player.push(data_distance_player['distance_40_45']);
    result_distance_player.push(data_distance_player['distance_45_50']);
    result_distance_player.push(data_distance_player['distance_50_60']);
    result_distance_player.push(data_distance_player['distance_60_70']);
    result_distance_player.push(data_distance_player['distance_70_80']);
    result_distance_player.push(data_distance_player['distance_80_90']);


    console.log("DISTANCE: ");
    console.log(result_distance_player);
    draw_chart_distance(result_distance_player);
  });
}




function retrieve_sprints(id_jugador_jornada){
  var url = new URL('https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/wimu/sprints_player');

  var params = { id_jugador_jornada:id_jugador_jornada }; // or:

  url.search = new URLSearchParams(params).toString();

  const sprints_player_response = fetch(url);

  sprints_player_response.then((response) =>{

  return response.json();

  }).then((items) => {
    const data_sprints_player = items.items[0];

    var result_sprints_player = []

    result_sprints_player.push(data_sprints_player['sprints_0_10']);
    result_sprints_player.push(data_sprints_player['sprints_10_20']);
    result_sprints_player.push(data_sprints_player['sprints_20_30']);
    result_sprints_player.push(data_sprints_player['sprints_30_40']);
    result_sprints_player.push(data_sprints_player['sprints_40_45']);
    result_sprints_player.push(data_sprints_player['sprints_45_50']);
    result_sprints_player.push(data_sprints_player['sprints_50_60']);
    result_sprints_player.push(data_sprints_player['sprints_60_70']);
    result_sprints_player.push(data_sprints_player['sprints_70_80']);
    result_sprints_player.push(data_sprints_player['sprints_80_90']);


    console.log("SPRINTS: ");
    console.log(result_sprints_player);
    draw_chart_sprints(result_sprints_player);
  });
}


function retrieve_hse(id_jugador_jornada){
  var url = new URL('https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/wimu/hse_player');

  var params = { id_jugador_jornada:id_jugador_jornada }; // or:

  url.search = new URLSearchParams(params).toString();

  const sprints_player_response = fetch(url);

  sprints_player_response.then((response) =>{

  return response.json();

  }).then((items) => {
    const data_hse_player = items.items[0];

    var result_hse_player = []

    result_hse_player.push(data_hse_player['hse_0_10']);
    result_hse_player.push(data_hse_player['hse_10_20']);
    result_hse_player.push(data_hse_player['hse_20_30']);
    result_hse_player.push(data_hse_player['hse_30_40']);
    result_hse_player.push(data_hse_player['hse_40_45']);
    result_hse_player.push(data_hse_player['hse_45_50']);
    result_hse_player.push(data_hse_player['hse_50_60']);
    result_hse_player.push(data_hse_player['hse_60_70']);
    result_hse_player.push(data_hse_player['hse_70_80']);
    result_hse_player.push(data_hse_player['hse_80_90']);


    console.log("HSE: ");
    console.log(result_hse_player);
    draw_chart_hse(result_hse_player);
  });
}



function draw_chart_distance(result) {
  var distance_canvas = document.getElementById('distance-chart').getContext('2d');
    var distance_chart = new Chart(distance_canvas, {
        type: 'bar',
        data: {
            labels: X_INTERVAL,
            datasets: [{
              label:'',
                data: result, //retrieve de data from the api
                backgroundColor: [

                    'rgba(54, 162, 235, 0.2)'

                ],
                borderColor: [

                    'rgba(54, 162, 235, 1)'

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



function draw_chart_sprints(result_sprints) {
  var sprint_canvas = document.getElementById('sprints-chart').getContext('2d');
    var sprints_chart = new Chart(sprint_canvas, {
        type: 'line',
        data: {
            labels: X_INTERVAL,
            datasets: [{
                label: '',
                data: result_sprints, //retrieve de data from the api
                backgroundColor: [

                    'rgba(54, 162, 235, 0.2)' //Azul
              ],
                borderColor: [
                  'rgba(54, 162, 235, 1)'//Azul
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



function draw_chart_hse(result_hse) {
  var hse_canvas = document.getElementById('hse-chart').getContext('2d');
    var hse_chart = new Chart(hse_canvas, {
        type: 'bar',
        data: {
            labels: X_INTERVAL,
            datasets: [{
                data: result_hse, //retrieve de data from the api
                backgroundColor: [

                    'rgba(54, 162, 235, 0.2)'//Azul

                ],
                borderColor: [

                    'rgba(54, 162, 235, 1)' //Azul

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



function draw_chart_position_golstats(result) {
  var position_canvas = document.getElementById('position-chart');

  const position_data = {
    labels: [
      'etiqueta 1',
        'etiqueta 2',
        'etiqueta 3',
        'etiqueta 4',
        'etiqueta 5',
        'etiqueta 6',
        'etiqueta 7',
        'etiqueta 8',
        'etiqueta 9',
        'etiqueta 10',
        'etiqueta 11',
        'etiqueta 12',
        'etiqueta 13',
        'etiqueta 14',

    ],
    datasets: [{
      label: 'Equipo Local',
      data: result,
      fill: true,
      backgroundColor: 'rgba(54, 162, 235, 0.2)',//Azul
      borderColor:   'rgba(54, 162, 235, 1)' ,//Azul
      pointBackgroundColor: 'rgba(54, 162, 235, 1)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgb(255, 99, 132)'
    } ]
  };


  var radarChart_position = new Chart(position_canvas, {
    type: 'radar',
    data: position_data,
    options:{
        responsive: true,
        maintainAspectRatio: false
    }
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
      backgroundColor: 'rgba(54, 162, 235, 0.2)',//Azul
      borderColor:   'rgba(54, 162, 235, 1)' ,//Azul
      pointBackgroundColor: 'rgba(54, 162, 235, 1)',
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





function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
