


fetchData(API,function (error1, data1){
  if(error1) return console.error(error1);
  fetchData(API + data1.items[0].id_jornada,function (error2, data2){
    if (error2) return console.error(error2);
    fetchData(data2.origin.url, function (error3, data3){
      if (error3) return console.error(error3);
      console.log(data1.items[0].id_jornada);
      console.log(data2.name);
      console.log(data3.dimension);
    });
  }

})
