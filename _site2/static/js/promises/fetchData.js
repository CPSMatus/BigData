let XMLHttpsRequest = require('xmlhttprequest');

const fetchData = (url_api) => {
  return new Promise((resolve, reject) =>{
    let xhttp = new XMLHttpsRequest();
    xhttp.open('GET',url_api,true);
    xhttp.onreadystatechange = ((){
      if(xhttp.readyState === 4){

        if (xhttp.status === 200 )
        ? resolve (JSON.parse(xhttp.responseText))
        : reject (new Error('Error ', url_api))
      }


    });
    xhttp.send();
  });

}

module.exports = fetchData;
