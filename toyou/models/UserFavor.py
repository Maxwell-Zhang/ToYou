# coding:utf-8
from toyou import db

class UserFavor(db.Model):
    __tablename__ = 'user_favor'
    userid = db.Column(db.Integer, primary_key=True)
    tag0 = db.Column(db.Integer, nullable=True)
    tag1 = db.Column(db.Integer, nullable=True)
    tag2 = db.Column(db.Integer, nullable=True)
    tag3 = db.Column(db.Integer, nullable=True)
    tag4 = db.Column(db.Integer, nullable=True)
    tag5 = db.Column(db.Integer, nullable=True)
    tag6 = db.Column(db.Integer, nullable=True)
    tag7 = db.Column(db.Integer, nullable=True)
    tag8 = db.Column(db.Integer, nullable=True)
    tag9 = db.Column(db.Integer, nullable=True)

    def __init__(self, userid, tag0=0, tag1=0, tag2=0, tag3=0, tag4=0, tag5=0, tag6=0, tag7=0, tag8=0, tag9=0):
        self.userid= userid
        self.tag0 = tag0
        self.tag1 = tag1
        self.tag2 = tag2
        self.tag3 = tag3
        self.tag4 = tag4
        self.tag5 = tag5
        self.tag6 = tag6
        self.tag7 = tag7
        self.tag8 = tag8
        self.tag9 = tag9

    def __repr__(self):
        return '<User: userid  = ' + self.userid + '>'
