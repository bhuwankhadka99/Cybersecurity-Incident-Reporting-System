from flask import Flask
from flask_login import LoginManager
from config import Config
from models import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@app.route("/")
def home():
    return "<h1>Cybersecurity Incident Reporting System</h1><p>Flask is connected successfully!</p>"

from routes import routes
app.register_blueprint(routes)

print(app.url_map) 
if __name__ == "__main__":
    app.run(debug=True)
    

