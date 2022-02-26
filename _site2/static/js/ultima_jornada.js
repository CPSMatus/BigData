myFunction();

function myFunction() {
  var jugador_alias_mayus = document.getElementById("jugador_uno");
  var low = jugador_alias_mayus.toString().toLowerCase();
  jugador_alias_mayus.innerHTML = 'Hola';
//  const myArray1 = jugador_alias_mayus.split(' ');
  console.log(low)
  return low

}
