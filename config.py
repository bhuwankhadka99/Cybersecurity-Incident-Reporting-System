import os

class Config:
    SECRET_KEY = "change_this_to_a_random_secret_key"

    SQLALCHEMY_DATABASE_URI = (
        "mysql+pymysql://root:NewPassword123!@localhost/incident_reporting_db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False