#coding:utf-8
import string
import os
#import sys
#sys.path.append('toyou/helpers/')
#import Image
from toyou import app,db
from toyou.helpers.UserHelper import addPostByQq
from toyou.models.Post import Post
from toyou.models.User import User
from toyou.models.UserFavor import UserFavor
from flask import Flask,redirect,url_for,Blueprint,request,jsonify,Response
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
def allowed_file(filename):
    return '.' in filename and \
           filename.split('.')[-1] in ALLOWED_EXTENSIONS

@app.route('/<name>',methods=['GET','POST'])
def get_image(name=None):
	print "request for " + str(name)
	if name:
	    image = file("./pic/{}".format(name))
	    resp = Response(image, mimetype="image/jpeg")
	    return resp

@app.route('/image_upload',methods=['GET','POST'])
def uploadImage():
	image_files = []
	for key in request.files.keys():
	    image_files.append(request.files.get(key))
	image_URL = []
        for file in image_files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_URL.append(os.path.join(app.config['UPLOAD_URL_PREFIX'] + str(app.config['PORT']), filename))
	#tag_id = getAITagId(image_files)
        tag_id = 1
	return jsonify(result=True,image_URL=image_URL,tag_id=tag_id)

@app.route('/new_message_upload',methods=['POST'])
def uploadMessage():
	qq =  request.form.get('account')
	content = request.form.get('message')
	imagelist = request.form.getlist('image_URL')
	tag = request.form.getlist('user_tag_id')
	addPostByQq(qq,content,tag,imagelist)
        return jsonify(result=True)

@app.route('/own_message',methods=['POST'])
def getOwnMessage():
	qq =  request.form.get('account')
	user = User.query.filter_by(qq=qq).first()
	own_message = Post.query.filter_by(userid=user.id).all()
	messages_ids = []
	for u in own_message:
		message_ids.append(u.id)
	return jsonify(result = True,message_ids=message_ids);
