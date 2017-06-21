
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from toyou.models.User import User
from toyou.models.Post import Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/toyou?charset=utf8mb4'

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)
manager = Manager(app)

if __name__ == '__main__':
   manager.run()

