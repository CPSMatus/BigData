const fetchData = require ('../promises/fetchData');


let API = 'https://g6d5f1265b0dcaf-dbapex.adb.us-ashburn-1.oraclecloudapps.com/ords/db_apex/jornada/ultima_jornada';

fetchData(API)
  .then( data => {
    console.log(data.info.count);
    return fetchData('${API}${data.results[0].id}')
  })
  .then(data =>{
    console.log(data.id_jornada);
    return fetchData(data.origin.url);
  })
  .then (data => {
    console.log.(data.dimension)
  })
  .catch(err => console.error(err))
