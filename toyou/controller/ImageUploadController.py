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

@app.route('/pic/<name>',methods=['GET','POST'])
def get_image(name=None):
	print "request for " + str(name)
	if name and allowed_file(name):
	    image = file("./pic/{}".format(name))
	    resp = Response(image, mimetype="image/jpeg")
	    return resp

@app.route('/image_upload',methods=['GET','POST'])
def uploadImage():
	content = request.form.get("message")
	qq = request.form.get("account")
	image_files = []
	for key in request.files.keys():
	    image_files.append(request.files.get(key))
	image_URL = []
        for file in image_files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                image_URL.append(os.path.join(app.config['UPLOAD_URL_PREFIX'] + str(app.config['PORT'])+"/pic/", filename))
	#tag_id = getAITagId(image_files)
        tag_id = 1
	message_id = addPostByQq(qq,content,tag,image_URL)	
	return jsonify(result='true',tag_id=tag_id,message_id = message_id)

@app.route('/new_message_upload',methods=['GET','POST'])
def uploadMessage():
	postid =  request.form.get('message_id')
	tag = request.form.get('tag')
	post = Post.query.filter_by(id=postid).first()
	post.tag = int(tag)
	db.session.commit()
        return jsonify(result='true')

@app.route('/own_message',methods=['GET','POST'])
def getOwnMessage():
	if request.method == "POST":
		qq =  request.form.get('account')
	if request.method == "GET":
		qq = request.args.get('account')
	user = User.query.filter_by(qq=qq).first()
	own_message = Post.query.filter_by(userid=user.id).all()
	messages_ids = []
	for u in own_message:
		messages_ids.append(u.id)
	result = []
    	for MessageId in messages_ids:
    		post = Post.query.filter_by(id=MessageId).first()
    		if post is None:
       	   		return jsonify({'state': 404, 'error': 'invalid msg id'})
    		data = { \
       	    	'message_id': post.id, \
            	'message': post.content, \
	    	'postdate': post.posttime.strftime('%Y-%m-%d'), \
           	'posttime': post.posttime.strftime('%H:%M'), \
            	'username': User.query.filter_by(id=post.userid).first().username \
            	}
		image = []
		image.append(post.image0)
		image.append(post.image1)
		image.append(post.image2)
		image.append(post.image3)
		image.append(post.image4)
		image.append(post.image5)
		image.append(post.image6)
		image.append(post.image7)
		image.append(post.image8)
		image2 = []
		for img in image:
	    		if  img!= '':
				image2.append(app.config['UPLOAD_URL_PREFIX']+str(app.config['PORT'])+"/"+app.config["UPLOAD_FOLDER"].split('/')[-1]+'/'+img.split('/')[-1])
		data['img_url'] = image2
		result.append(data)
    	return jsonify({'state': 200, 'error': '', 'data': result})

