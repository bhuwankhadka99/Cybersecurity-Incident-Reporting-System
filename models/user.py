from flask_login import UserMixin
from models import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum("Admin", "User"), default="User")
    created_at = db.Column(db.DateTime)

    incidents = db.relationship(
        "Incident",
        backref="user",
        lazy=True
    )

    activity_logs = db.relationship(
        "ActivityLog",
        backref="user",
        lazy=True
    )  