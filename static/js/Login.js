console.log("login.js loaded");
document.getElementById("loginForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    console.log("Login button clicked");

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: email,
            password: password
        })
    });

    const result = await response.json();
    console.log("Status:", response.status);
    console.log("Result:", result);

    document.getElementById("message").innerText =
        result.message || result.error;

    // If login is successful, go to the dashboard
    if (response.ok) {
        setTimeout(function () {
            window.location.href = "/dashboard";
        }, 1000);
    }
});