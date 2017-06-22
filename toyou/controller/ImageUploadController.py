#coding:utf-8
import string
import os
#import sys
#sys.path.append('toyou/helpers/')
#import Image
from toyou import app,db
from toyou.helpers.UserHelper import addPostByName
from toyou.models.Post import Post
from toyou.models.User import User
from toyou.models.UserFavor import UserFavor
from flask import Flask,redirect,url_for,Blueprint,request,jsonify
from werkzeug import secure_filename
UPLOAD_FOLDER = './pic'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
else:
    pass
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

bp = Blueprint('Zx',__name__)
@bp.route('/image_upload',methods=['POST'])
def uploadImage():
	image_files = request.files.getlist('image[]')
	image_URL = []
        for file in image_files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_URL.append(os.path.join(app.config['UPLOAD_FOLDER'], filename))
	#tag_id = getAITagId(image_files)
        tag_id = 1
	return jsonify(result='true',image_URL=image_URL,tag_id=tag_id)

	
@bp.route('/new_message_upload',methods=['POST'])
def uploadMessage():
	qq =  request.form.get('account')
	content = request.form.get('message')
	imagelist = request.form.getlist('image_URL')
	tag = request.form.getlist('user_tag_id')
        user = User.query.filter_by(qq=qq).first()
	addPostByname(user.username,content,tag,imagelist)
        return jsonify(result='true')

@bp.route('/own_message',methods=['POST'])
def getOwnMessage():
	qq =  request.form.get('account')
	user = User.query.filter_by(qq=qq).first()
	own_message = Post.query.filter_by(userid=user.id).all()
	messages_ids = []
	for u in own_message:
		message_ids.append(u.id)
	return jsonify(result = 'true',message_ids=message_ids);
app.register_blueprint(bp,url_prefix='/Zx')
