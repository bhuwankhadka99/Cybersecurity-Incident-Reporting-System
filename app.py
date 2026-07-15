from flask import Flask, render_template, redirect
# from flask_login import LoginManager
from config import Config
from models import db
from models import User, Category, Incident, ActivityLog

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    print(db.metadata.tables.keys())
    db.create_all()

# ---------------- HOME ----------------
@app.route("/")
def home():
    return redirect("/login-page")


# ---------------- REGISTER PAGE ----------------
@app.route("/register-page")
def register_page():
    return render_template("register.html")


# ---------------- LOGIN PAGE ----------------
@app.route("/login-page")
def login_page():
    return render_template("login.html")


# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ---------------- CREATE INCIDENT PAGE ----------------
@app.route("/create-incident-page")
def create_incident_page():
    return render_template("create_incident.html")


# ---------------- VIEW INCIDENTS PAGE ----------------
@app.route("/incidents-page")
def incidents_page():
    return render_template("incidents.html")


# ---------------- ACTIVITY LOG PAGE ----------------
@app.route("/activity-logs-page")
def activity_logs_page():
    return render_template("activity_logs.html")


# Register API routes
from routes import routes
app.register_blueprint(routes)

print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)