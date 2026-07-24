const params = new URLSearchParams(window.location.search);
const incidentId = params.get("id");

// Load the current incident data
fetch(`/incidents/${incidentId}`)
.then(response => response.json())
.then(data => {

    document.getElementById("title").value = data.title;
    document.getElementById("description").value = data.description;
    document.getElementById("severity").value = data.severity;
    document.getElementById("status").value = data.status;

});

// Update the incident
document.getElementById("editForm").addEventListener("submit", async function(event) {

    event.preventDefault();

    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    const severity = document.getElementById("severity").value;
    const status = document.getElementById("status").value;

    const response = await fetch(`/incident/${incidentId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title,
            description,
            severity,
            status
        })
    });

    const result = await response.json();

    document.getElementById("message").innerText = result.message;

    if (response.ok) {
        setTimeout(function () {
            window.location.href = "/incidents-page";
        }, 1000);
    }
});