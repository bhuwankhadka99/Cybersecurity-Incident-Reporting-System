fetch("/activity-logs")
.then(response => response.json())
.then(data => {

    const table = document.getElementById("logTable");

    data.logs.forEach(function(log){

        table.innerHTML += `
        <tr>
            <td>${log.id}</td>
            <td>${log.user_id}</td>
            <td>${log.action}</td>
            <td>${log.timestamp}</td>
        </tr>
        `;
    });

});