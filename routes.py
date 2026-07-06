from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

routes = Blueprint("routes", __name__)


@routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    # find user
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    # check password
    if not check_password_hash(user.password, password):
        return jsonify({"error": "Incorrect password"}), 401

    return jsonify({
        "message": "Login successful",
        "user": {
            "username": user.username,
            "email": user.email
        }
    }), 200

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Check for missing fields
    if not username or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    # Check if username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400

    # Check if email already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 400

    # Hash the password
    hashed_password = generate_password_hash(password)

    # Create new user
    new_user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201
 