from models import db


class Incident(db.Model):
    __tablename__ = "incidents"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    severity = db.Column(
        db.Enum("Low", "Medium", "High", "Critical"),
        nullable=False
    )
    status = db.Column(
        db.Enum("Open", "In Progress", "Resolved"),
        default="Open"
    )
    reported_by = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )
    created_at = db.Column(db.DateTime)