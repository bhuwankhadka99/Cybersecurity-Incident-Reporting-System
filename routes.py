from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Incident, ActivityLog


routes = Blueprint("routes", __name__)


# ---------------- REGISTER ----------------
@routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already exists"}), 400

    hashed_password = generate_password_hash(password)

    new_user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


# ---------------- LOGIN ----------------
@routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON data"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    if not check_password_hash(user.password, password):
        return jsonify({"error": "Incorrect password"}), 401

    return jsonify({
        "message": "Login successful",
        "user": {
            "username": user.username,
            "email": user.email
        }
    }), 200


# ---------------- CREATE INCIDENT ----------------
@routes.route("/incident", methods=["POST"])
def create_incident():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    title = data.get("title")
    description = data.get("description")
    category_id = data.get("category_id")
    severity = data.get("severity")
    status = data.get("status", "Open")
    user_id = data.get("user_id")

    if not title or not description or not category_id or not severity or not user_id:
        return jsonify({"error": "All fields are required"}), 400

    new_incident = Incident(
        title=title,
        description=description,
        category_id=category_id,
        severity=severity,
        status=status,
        user_id=user_id
    )

    db.session.add(new_incident)
    db.session.commit()

    log = ActivityLog(
        user_id=user_id,
        action="Created Incident"
    )

    db.session.add(log)
    db.session.commit()

    return jsonify({"message": "Incident created successfully"}), 201
# ---------------- GET INCIDENTS ----------------
@routes.route("/incidents", methods=["GET"])
def get_incidents():
    incidents = Incident.query.all()

    output = []

    for incident in incidents:
        output.append({
            "id": incident.id,
            "title": incident.title,
            "description": incident.description,
            "severity": incident.severity,
            "status": incident.status,
            "user_id": incident.user_id
        })

    return jsonify({"incidents": output}), 200