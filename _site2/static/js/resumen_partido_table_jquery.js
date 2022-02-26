

async function retrieve_jornada_info(){
  $.ajax({
    url: "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/ultima_jornada",
    type: "get",
    dataType:"json",
    success: function(response){
      fecha_y_hora = response['items'][0]['fecha']
      arbitro = ( response['items'][0]['nombre_arbitraje'] ) + ( response['items'][0]['apellido_arbitraje'] )
      //Split fecha y hora

      fecha = document.getElementById("fecha").innerHTML = fecha_y_hora;

      hora = document.getElementById("hora").innerHTML = fecha_y_hora;

      abitraje = document.getElementById("arbitraje").innerHTML = "Arbitró: " + arbitro;

      console.log(response);
    },
    error: function(error){
      console.log(error);
    }
  })


}


$(document).ready(function(){
  retrieve_jornada_info();
})



async function retrieve_golstats_general(){
  $.ajax({
    url: "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/golstats/general_golstats",
    type: "get",
    data: {
    id_jornada: 46,
    },
    dataType:"json",
    success: function(response){


      var response_array = response['items'][0];
    //  console.log(response_array);

      t_amarillas = document.getElementById("total_amarillas").innerHTML = "Total amarillas: " + response_array.tarjetas_amarillas ;

      t_rojas = document.getElementById("total_rojas").innerHTML =  "Total rojas: " + response_array.tarjetas_rojas ;

    },
    error: function(error){
      console.log(error);
    }
  })
}



async function retrieve_golstats_defensiva(){
  $.ajax({
    url: "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/golstats/ofensiva_golstats",
    type: "get",
    data: {
    id_jornada: 46,
    id_equipo: 18
    },
    dataType:"json",
    success: function(response){

      var response = response['items'][0];

      //Convert response into an array
      var result = []

      result.push(response.pases_acertados_cancha_propia);
      result.push(response.pases_no_acertados_cancha_propia);
      result.push(response.pases_acertados_cancha_rival);
      result.push(response.pases_no_acertados_cancha_rival);
      //result.push(response.goles);
      result.push(response.tiros_a_gol);
      result.push(response.faltas_recibidas);
      result.push(response.uno_vs_uno_exitoso_ofensivo);
      result.push(response.uno_vs_uno_no_exitoso_ofensivo);

      draw_chart_defensiva_golstats(result)

    },
    error: function(error){
      console.log(error);
    }
  })
}


$(document).ready(function(){
  retrieve_golstats_general();
  retrieve_golstats_ofensiva();
  retrieve_golstats_defensiva();
})


function draw_chart_defensiva_golstats(results) {
  var defensiva_canvas = document.getElementById('ofensiva-chart');

  const defensiva_data = {
    labels: [
      'Pases acertados cancha propia',
      'pases no acertados cancha propia',
      'pases acertados cancha rival',
      'pases no acertados cancha rival',
      //'goles',
      'tiros a gol',
      'faltas recibidas',
      '1 vs 1 exitoso ofensivo',
      '1 vs 1 no exitoso ofensivo'
    ],
    datasets: [{
      label: 'Equipo Local',
      data: results,
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


async function retrieve_jugadores_info(){
  $.ajax({
    url: "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/jugadores_jornada",
    type: "get",
    data: {
    id_jornada: 46
    },
    dataType:"json",
    success: function(response){
      const datos_jugadores = response.items[0];
      //append all the items to an array
      console.log(datos_jugadores)


    },
    error: function(error){
      console.log(error);
    }
  })
}



async function retrieve_distance_team_info(){
  $.ajax({
    url: "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/wimu/wimu_distance_team",
    type: "get",
    data: {
    id_jornada: 46
    },
    dataType:"json",
    success: function(response){
      const data_hse = response.items[0];
      //append all the items to an array
      var result_distance_team = []
      for(var i in data_hse){
        result_distance_team.push(data_hse[i]);
      }
      console.log(result_distance_team);



    },
    error: function(error){
      console.log(error);
    }
  })
}


$(document).ready(function(){
  retrieve_distance_team_info();
})



async function retrieve_golstats_ofensiva(){
  $.ajax({
    url: "https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/golstats/ofensiva_golstats",
    type: "get",
    data: {
    id_jornada: 46,
    id_equipo: 18
    },
    dataType:"json",
    success: function(response){

      var response = response['items'][0];

      //Convert response into an array
      var result = []

      result.push(response.pases_acertados_cancha_propia);
      result.push(response.pases_no_acertados_cancha_propia);
      result.push(response.pases_acertados_cancha_rival);
      result.push(response.pases_no_acertados_cancha_rival);
      //result.push(response.goles);
      result.push(response.tiros_a_gol);
      result.push(response.faltas_recibidas);
      result.push(response.uno_vs_uno_exitoso_ofensivo);
      result.push(response.uno_vs_uno_no_exitoso_ofensivo);

      draw_chart_ofensiva_golstats(result)

    },
    error: function(error){
      console.log(error);
    }
  })
}


function draw_chart_ofensiva_golstats(results) {
  var ofensiva_canvas = document.getElementById('ofensiva-chart');

  const ofensiva_data = {
    labels: [
      'Pases acertados cancha propia',
      'pases no acertados cancha propia',
      'pases acertados cancha rival',
      'pases no acertados cancha rival',
      //'goles',
      'tiros a gol',
      'faltas recibidas',
      '1 vs 1 exitoso ofensivo',
      '1 vs 1 no exitoso ofensivo'
    ],
    datasets: [{
      label: 'Equipo Local',
      data: results,
      fill: true,
      backgroundColor: 'rgba(255, 99, 132, 0.2)',
      borderColor: 'rgb(255, 99, 132)',
      pointBackgroundColor: 'rgb(255, 99, 132)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgb(255, 99, 132)'
    } /*, {
      label: 'My Second Dataset',
      data: [28, 48, 40, 19, 96, 27, 100],
      fill: true,
      backgroundColor: 'rgba(54, 162, 235, 0.2)',
      borderColor: 'rgb(54, 162, 235)',
      pointBackgroundColor: 'rgb(54, 162, 235)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgb(54, 162, 235)'
    }*/]
  };


  var radarChart_ofensiva = new Chart(ofensiva_canvas, {
    type: 'radar',
    data: ofensiva_data
  });

}
