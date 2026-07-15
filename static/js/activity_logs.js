function loadLogs(){


fetch("/activity-logs")


.then(response => response.json())


.then(data => {


let table = document.getElementById("logsTable");


table.innerHTML="";



data.logs.forEach(log => {


let row = `


<tr>


<td>${log.id}</td>


<td>${log.user_id}</td>


<td>${log.action}</td>


<td>${log.timestamp}</td>


</tr>


`;


table.innerHTML += row;


});


})


.catch(error => {

console.log(error);

});


}



loadLogs();