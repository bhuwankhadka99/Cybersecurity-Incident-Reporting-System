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
                <button onclick="updateIncident(${incident.id})">
                    Update
                </button>

                <button onclick="deleteIncident(${incident.id})">
                    Delete
                </button>
            </td>
        </tr>
        `;
    });

});


function updateIncident(id) {

    window.location.href = `/edit-incident?id=${id}`;

}

function deleteIncident(id) {

    if(confirm("Are you sure you want to delete this incident?")) {

        fetch(`/incidents/${id}`, {
            method: "DELETE"
        })

        .then(response => response.json())

        .then(data => {

            alert(data.message);

            location.reload();

        
        })
        .catch(error => {
            console.error(error);
        });


    }

}