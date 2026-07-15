from flask import Blueprint, redirect, request, jsonify, render_template
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Incident, ActivityLog


routes = Blueprint("routes", __name__)


# ---------------- CREATE INCIDENT PAGE ----------------
@routes.route("/create-incident")
@login_required
def create_incident_page():
    return render_template("create_incident.html")

# ---------------- ACTIVITY LOGS PAGE ----------------
@routes.route("/activity-logs-page")
def activity_logs_page():
    return render_template("activity_logs.html")


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


    activity = ActivityLog(
        user_id=new_user.id,
        action="User Registered"
    )

    db.session.add(activity)
    db.session.commit()


    return jsonify({
        "message": "User registered successfully"
    }), 201



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
    login_user(user)


    activity = ActivityLog(
        user_id=user.id,
        action="User Logged In"
    )

    db.session.add(activity)
    db.session.commit()



    return jsonify({
        "message": "Login successful",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }), 200

# ---------------- LOGOUT ----------------
@routes.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect("/login-page")




# ---------------- CREATE INCIDENT API ----------------
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



    activity = ActivityLog(

        user_id=user_id,
        action="Created Incident"

    )


    db.session.add(activity)
    db.session.commit()



    return jsonify({
        "message": "Incident created successfully"
    }), 201

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

    return jsonify({
        "incidents": output
    }), 200


# ---------------- GET SINGLE INCIDENT ----------------
@routes.route("/incidents/<int:id>", methods=["GET"])
def get_single_incident(id):

    incident = Incident.query.get(id)

    if not incident:
        return jsonify({"error": "Incident not found"}), 404

    return jsonify({
        "id": incident.id,
        "title": incident.title,
        "description": incident.description,
        "severity": incident.severity,
        "status": incident.status,
        "user_id": incident.user_id
    }), 200





# ---------------- UPDATE INCIDENT ----------------
@routes.route("/incident/<int:id>", methods=["PUT"])
def update_incident(id):

    incident = Incident.query.get(id)


    if not incident:
        return jsonify({"error": "Incident not found"}), 404



    data = request.get_json()



    if "title" in data:
        incident.title = data["title"]


    if "description" in data:
        incident.description = data["description"]


    if "severity" in data:
        incident.severity = data["severity"]


    if "status" in data:
        incident.status = data["status"]



    db.session.commit()


    return jsonify({
        "message": "Incident updated successfully"
    }), 200






# ---------------- DELETE INCIDENT ----------------
@routes.route("/incident/<int:id>", methods=["DELETE"])
def delete_incident(id):

    incident = Incident.query.get(id)


    if not incident:
        return jsonify({"error": "Incident not found"}), 404



    db.session.delete(incident)
    db.session.commit()



    return jsonify({
        "message": "Incident deleted successfully"
    }), 200






# ---------------- GET ACTIVITY LOGS ----------------
@routes.route("/activity-logs", methods=["GET"])
def get_activity_logs():

    logs = ActivityLog.query.all()

    output = []


    for log in logs:

        output.append({

            "id": log.id,
            "user_id": log.user_id,
            "action": log.action,
            "timestamp": str(log.timestamp)

        })


    return jsonify({
        "logs": output
    }), 200

# ---------------- EDIT INCIDENT PAGE ----------------
@routes.route("/edit-incident")
def edit_incident_page():

    return render_template("edit_incident.html")