# coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

app = Flask(__name__)
print "__name__ = " + __name__
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/toyou?charset=utf8mb4'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
manager = Manager(app)
from controller import UserController
from controller import GetMessageController
from controller import ImageUploadController
from controller import PostController
from controller import UserFavorController
#from controller import RunController
#from controller import EquipmentController
#from controller import PkController
#from controller import ShareController

if __name__ == "__main__":
    manager.run()
