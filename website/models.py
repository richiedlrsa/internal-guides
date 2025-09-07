from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin

class Guide(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable = False)
    content = db.Column(db.String, nullable = False)
    created_at = db.Column(db.DateTime(timezone = True), nullable = False, default = func.now())
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
    role = db.Column(db.String, nullable=False, default='user')
    created_at = db.Column(db.DateTime(timezone = True), nullable = False, default = func.now())