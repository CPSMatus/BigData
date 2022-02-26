
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
  const  title  = document.getElementById("h_jornada").innerHTML = " en Jornada " +  jornada['n_jornada'] ;


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
    const  jugador_alias  = document.getElementById("span-card-1").innerHTML = jugar_nombre ;
    const jugador_title =  document.getElementById("h_jugador").innerHTML = "Analisis de " + jugar_nombre + " ";
    const  tiempo_juego = document.getElementById("tiempo_juego").innerHTML = jugador ['minutos_jugados'] + ' min' ;

    const  distancia_total = document.getElementById("distancia_total").innerHTML;

    const  entra = document.getElementById("entra").innerHTML = 'min ' + jugador['entra'] + "' ";

    const  sale = document.getElementById("sale").innerHTML = 'min '+ jugador['sale'] + "' " ;


    console.log(jugador);
    const jugador_id = jugador['jugador_jornada_id']
    retrieve_distance(jugador_id);
    retrieve_sprints(jugador_id);
    retrieve_hse(jugador_id);

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
    var counter = 1;

    for(var i in data_distance_player){

      if (counter == 1){
        counter = counter + 1;
        continue;
      }
      result_distance_player.push(data_distance_player[i]);
      counter = counter + 1;
    }
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
    var counter = 1;

    for(var i in data_sprints_player){

      if (counter == 1){
        counter = counter + 1;
        continue;
      }
      result_sprints_player.push(data_sprints_player[i]);
      counter = counter + 1;
    }
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
    var counter = 1;

    for(var i in data_hse_player){

      if (counter == 1){
        counter = counter + 1;
        continue;
      }
      result_hse_player.push(data_hse_player[i]);
      counter = counter + 1;
    }
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



function draw_chart_hse(result_hse) {
  var hse_canvas = document.getElementById('hse-chart').getContext('2d');
    var hse_chart = new Chart(hse_canvas, {
        type: 'bar',
        data: {
            labels: X_INTERVAL,
            datasets: [{
                data: result_hse, //retrieve de data from the api
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
