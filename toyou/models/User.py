# coding:utf-8
from runtob import db
from sqlalchemy.dialects import mysql


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    token = db.Column(db.String(32), nullable=True)
    valid = db.Column(mysql.ENUM('Y', 'N'), nullable=False)
    lastLogin = db.Column(db.DateTime, nullable=False)
    money = db.Column(db.Integer, nullable=False)
    total_step = db.Column(db.Integer, nullable=False)

    def __init__(self, username, token, valid='Y', lastLogin='', money=0, total_step=0):
        self.username = username
        self.token = token
        self.valid = valid
        self.lastLogin = lastLogin
        self.money = money
        self.total_step = total_step

    def __repr__(self):
        return '<User %r>' % (self.username)
