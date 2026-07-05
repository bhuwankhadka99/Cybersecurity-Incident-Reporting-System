from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def home():
    return "<h1>Cybersecurity Incident Reporting System</h1><p>Flask is connected successfully!</p>"
import routes  

if __name__ == "__main__":
    app.run(debug=True)
    
