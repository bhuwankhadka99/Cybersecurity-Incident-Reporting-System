from flask import Flask, render_template
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

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "routes.login"


# ---------------- HOME ----------------
@app.route("/")
def home():
    return "<h1>Cybersecurity Incident Reporting System</h1><p>Flask is connected successfully!</p>"


# ---------------- REGISTER PAGE ----------------
@app.route("/register-page")
def register_page():
    return render_template("register.html")


from routes import routes
app.register_blueprint(routes)

print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)