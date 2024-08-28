# models.py

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import db, login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    trucks = db.relationship('Truck', backref='owner', lazy=True)

class Truck(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    truck_id = db.Column(db.String(50), nullable=False)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    odometer = db.Column(db.Float, nullable=False)
    fuel = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    trips = db.relationship('Trip', backref='truck', lazy=True)

class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    start_location = db.Column(db.String(100))
    end_location = db.Column(db.String(100))
    distance_covered = db.Column(db.Float)
    truck_id = db.Column(db.Integer, db.ForeignKey('truck.id'), nullable=False)
