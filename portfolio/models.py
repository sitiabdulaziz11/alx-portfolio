from datetime import datetime
from portfolio import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)  # password as plain text.
    
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"
