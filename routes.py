from flask import request, jsonify
from app import app, db
from models import User


@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Create new user
    new_user = User(
        username=username,
        email=email,
        password=password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"})