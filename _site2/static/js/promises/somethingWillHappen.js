const somethingWillHappen = () =>{
  return new Promise((resolve, reject ) => {
    if (true){
      resolve ("Hey!");
    } else {
      reject ("Whoops!");
    }
  });
};

somethingWillHappen()
.then(response => console.log(response))
.catch(err => console.error(err));
