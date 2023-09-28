from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    second_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    # created_at = db.Column(db.DateTime, default=datetime.utcnow)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, first_name, second_name, email, password):
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.password = password


    def __repr__(self):
        return f'User({self.second_name}, {self.email})'