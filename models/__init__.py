from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .category import Category
from .incident import Incident
from .activity_log import ActivityLog
