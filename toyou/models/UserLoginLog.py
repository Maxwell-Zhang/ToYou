# coding: utf-8
from runtob import db
from sqlalchemy import ForeignKey


class UserLoginLog(db.Model):
    __tablename__ = 'user_login_log'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userId = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    loginTime = db.Column(db.DateTime, nullable=False)
    locationX = db.Column(db.Float, nullable=False)
    locationY = db.Column(db.Float, nullable=False)

    def __init__(self, userId, loginTime, locationX, locationY):
        self.userId = userId
        self.loginTime = loginTime
        self.locationX = locationX
        self.locationY = locationY
