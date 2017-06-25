# coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

app = Flask(__name__)
print "__name__ = " + __name__
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/toyou?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['UPLOAD_FOLDER'] = '/home/ubuntu/ToYou/pic'
app.config['UPLOAD_URL_PREFIX'] = 'http://111.231.110.120:'
app.config['PORT'] = 5006
db = SQLAlchemy(app, use_native_unicode="utf8")
manager = Manager(app)
from controller import UserController
from controller import GetMessageController
from controller import ImageUploadController
from controller import PostController
from controller import UserFavorController
from controller import MessageController
#from controller import RunController
#from controller import EquipmentController
#from controller import PkController
#from controller import ShareController

#from controller import UserController
#from controller import GetMessageController
#from controller import ImageUploadController

#from tuyouAlgorithm.picture import picture_detection 
#import findmoment, sentence_score, getimageclassMap
from numpy import *
#allclassmean = load('/home/ubuntu/ToYou/toyou/tuyouAlgorithm/picture/allclassmean.npy')

if __name__ == "__main__":
    manager.run()

