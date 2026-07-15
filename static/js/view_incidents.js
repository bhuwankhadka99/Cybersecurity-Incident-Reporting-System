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

            <td>

            <button onclick="editIncident(${incident.id})">
            ✏️ Edit
            </button>


            <button onclick="deleteIncident(${incident.id})">
            🗑 Delete
            </button>


            </td>

            </tr>

            `;


            table.innerHTML += row;


        });


    })


    .catch(error => {

        console.log(error);

    });


}




function deleteIncident(id){


    if(confirm("Are you sure you want to delete this incident?")){


        fetch(`/incident/${id}`, {

            method:"DELETE"

        })


        .then(response => response.json())


        .then(data => {


            alert(data.message);


            loadIncidents();


        });


    }

}




function editIncident(id){


    let title = prompt("Enter new incident title:");

    let severity = prompt(
        "Enter severity (Low, Medium, High, Critical):"
    );


    if(title && severity){


        fetch(`/incident/${id}`,{


            method:"PUT",


            headers:{

                "Content-Type":"application/json"

            },


            body:JSON.stringify({

                title:title,

                severity:severity

            })


        })


        .then(response=>response.json())


        .then(data=>{


            alert(data.message);


            loadIncidents();


        });


    }

}




loadIncidents();