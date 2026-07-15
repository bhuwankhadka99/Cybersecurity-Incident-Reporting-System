fetch("/incidents")
.then(response => response.json())
.then(data => {

    const table = document.getElementById("incidentTable");

    data.incidents.forEach(function(incident){

        table.innerHTML += `
        <tr>
            <td>${incident.id}</td>
            <td>${incident.title}</td>
            <td>${incident.description}</td>
            <td>${incident.severity}</td>
            <td>${incident.status}</td>
            <td>${incident.user_id}</td>

            <td>
                <button onclick="deleteIncident(${incident.id})">
                    Delete
                </button>
            </td>
        </tr>
        `;
    });

});


async function deleteIncident(id){

    if(!confirm("Delete this incident?")){
        return;
    }

    const response = await fetch(`/incident/${id}`,{
        method:"DELETE"
    });

    const result = await response.json();

    alert(result.message);

    location.reload();

}