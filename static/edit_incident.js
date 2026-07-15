const params = new URLSearchParams(window.location.search);
const incidentId = params.get("id");

document.getElementById("editForm").addEventListener("submit", async function(event) {

    event.preventDefault();

    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    const severity = document.getElementById("severity").value;
    const status = document.getElementById("status").value;

    const response = await fetch(`/incidents/${incidentId}`, {
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