document.getElementById("incidentForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    const category_id = document.getElementById("category_id").value;
    const severity = document.getElementById("severity").value;
    const user_id = document.getElementById("user_id").value;

    const response = await fetch("/incident", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: title,
            description: description,
            category_id: category_id,
            severity: severity,
            status: "Open",
            user_id: user_id
        })
    });

    const result = await response.json();

    document.getElementById("message").innerText =
        result.message || result.error;
});