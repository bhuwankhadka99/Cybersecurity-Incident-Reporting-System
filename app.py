from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_required, current_user
from config import Config
from models import db
from models import User, Category, Incident, ActivityLog

app = Flask(__name__)

app.config.from_object(Config)


# ---------------- DATABASE ----------------
db.init_app(app)


with app.app_context():
    print(db.metadata.tables.keys())
    db.create_all()



# ---------------- FLASK LOGIN ----------------
login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = "login_page"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))





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
@login_required
def dashboard():
    return render_template("dashboard.html", username=current_user.username)





# ---------------- CREATE INCIDENT PAGE ----------------
@app.route("/create-incident-page")
@login_required
def create_incident_page():
    return render_template("create_incident.html")





# ---------------- VIEW INCIDENTS PAGE ----------------
@app.route("/incidents-page")
@login_required
def incidents_page():
    return render_template("incidents.html")





# ---------------- ACTIVITY LOG PAGE ----------------
@app.route("/activity-logs-page")
@login_required
def activity_logs_page():
    return render_template("activity_logs.html")





# ---------------- REGISTER API ROUTES ----------------
from routes import routes

app.register_blueprint(routes)





# Show all routes
print(app.url_map)




if __name__ == "__main__":
    app.run(debug=True)