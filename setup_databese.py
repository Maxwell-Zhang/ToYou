from toyou import app
from toyou import db
from toyou.models.User import User
from toyou.models.Post import Post
from toyou.models.UserFavor import UserFavor
db.drop_all()
db.create_all()
