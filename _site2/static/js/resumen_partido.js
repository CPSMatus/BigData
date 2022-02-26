
async function getTeamDistance(){
  const response = await fetch('');
  const data = await response.txt();

  const table = data.split('');
  console.log(data)
}
