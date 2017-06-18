# coding: utf-8
from runtob import db
from sqlalchemy.dialects import mysql


class UserProfile(db.Model):
    __tablename__ = 'user_profile'
    userId = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(50), nullable=False)
    gender = db.Column(mysql.ENUM('male', 'female', ''), nullable=False)
    phone = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    avatar = db.Column(db.String(200), nullable=False)

    def __init__(self, userId, nickname='', gender='', phone='', email='', avatar=''):
        self.userId = userId
        self.nickname = nickname
        self.gender = gender
        self.phone = phone
        self.email = email
        self.avatar = avatar
