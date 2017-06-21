# coding:utf-8
from toyou import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    qq = db.Column(db.Integer, unique=True, nullable=False)

    def __init__(self, username, qq):
        self.username = username
        self.qq = qq
    def __repr__(self):
        return '<User: username  = ' + self.username + ', qq = ' + str(self.qq) + '>'
