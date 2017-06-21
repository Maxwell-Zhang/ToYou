# coding: utf-8
from toyou import db
from sqlalchemy import ForeignKey
from datetime import datetime
class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    posttime = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.String(500), nullable=True)
    tag = db.Column(db.Integer, nullable=False)
    image0 = db.Column(db.String(500), nullable=True)
    image1 = db.Column(db.String(500), nullable=True)
    image2 = db.Column(db.String(500), nullable=True)
    image3 = db.Column(db.String(500), nullable=True)
    image4 = db.Column(db.String(500), nullable=True)
    image5 = db.Column(db.String(500), nullable=True)
    image6 = db.Column(db.String(500), nullable=True)
    image7 = db.Column(db.String(500), nullable=True)
    image8 = db.Column(db.String(500), nullable=True)
    image9 = db.Column(db.String(500), nullable=True)

    def __init__(self, userid, content="", tag=tag, image0 = "", image1= "",
        image2="", image3="", image4="", image5="", image6="", image7="", image8="", image9=""):
        self.userid = userid
        self.posttime = datetime.utcnow()
        self.content = content
        self.tag = tag
        self.image0 = image0
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3
        self.image4 = image4
        self.image5 = image5
        self.image6 = image6
        self.image7 = image7
        self.image8 = image8
        self.image9 = image9

    def __repr__(self):
        return '<Post: userid = ' + str(self.userid) + ', posttime = ' + str(self.posttime) + ', content = ' + str(self.content) + ', tag = ' + str(tag) + '>'
        

