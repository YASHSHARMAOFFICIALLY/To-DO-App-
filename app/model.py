from app import db
from flask_login import UserMixin
from datetime import datetime

class users(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(100),nullable = False,unique = True)
    password = db.Column(db.String(200),nullable = False)

class Task(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(100),nullable = False)
    status = db.Column(db.String(20),default = "Pending")
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    
   
