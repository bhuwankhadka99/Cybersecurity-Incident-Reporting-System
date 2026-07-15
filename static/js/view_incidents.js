function loadIncidents(){


fetch("/incidents")


.then(response => response.json())


.then(data => {


let table = document.getElementById("incidentTable");


table.innerHTML = "";



data.incidents.forEach(incident => {


let row = `

<tr>

<td>${incident.id}</td>

<td>${incident.title}</td>

<td>${incident.description}</td>

<td>${incident.severity}</td>

<td>${incident.status}</td>

<td>${incident.user_id}</td>

</tr>

`;


table.innerHTML += row;


});


})


.catch(error => {

console.log(error);

});


}



loadIncidents();