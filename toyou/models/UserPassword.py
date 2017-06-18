# coding: utf-8
from runtob import db


class UserPassword(db.Model):
    __tablename__ = 'user_password'
    userId = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(40), nullable=False)
    salt = db.Column(db.String(40), nullable=False)

    def __init__(self, userId, password, salt):
        self.userId = userId
        self.password = password
        self.salt = salt
