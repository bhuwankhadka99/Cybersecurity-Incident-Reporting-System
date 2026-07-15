document.getElementById("registerForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username: username,
            email: email,
            password: password
        })
    });

    const result = await response.json();

    document.getElementById("message").innerHTML =
        result.message || result.error;

    // If registration is successful, redirect to login page
    if (response.ok) {
        setTimeout(function () {
            window.location.href = "/login-page";
        }, 1000);
    }
});