# coding: utf-8
import redis

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config.from_object('config.DevelopmentConfig')
#r = redis.StrictRedis(host=app.config['REDIS_HOST'], password=app.config['REDIS_PASSWORD'],port=app.config['REDIS_PORT'])
db = SQLAlchemy(app)

from controller import UserController
from controller import GetMessageController
from controller import ImageUploadController
#from controller import RunController
#from controller import EquipmentController
#from controller import PkController
#from controller import ShareController
