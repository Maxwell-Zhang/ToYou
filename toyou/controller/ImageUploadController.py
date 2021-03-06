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
from toyou.tuyouAlgorithm.picture.picture_detection import *
from numpy import *
from toyou.helpers.UserHelper import *
from toyou.nsfw.classify_nsfw import *
#from toyou import allclassman

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#likecount = []
#commentcount = []
#import random
#for i in range(1000):
#    likecount.append(random.randint(3,15))
#    commentcount.append(random.randint(0,20))

def allowed_file(filename):
    return '.' in filename and \
           filename.split('.')[-1] in ALLOWED_EXTENSIONS

def reflect_class(class_id):
	reflect_array = [9,2,1,9,9,9,9,1,9,4, \
                         1,1,9,9,4,9,1,3,4,4, \
                         1,9,0,1,1,1,0,1,3,9, \
                         9,9,9,9,9,1,9,9,9,1, \
                         1,1,9,0,9,9,3,4,9,9]
	return reflect_array[int(class_id)]

@app.route('/pic/<name>',methods=['GET','POST'])
def get_image(name=None):
	print "request for " + str(name)
	if name and allowed_file(name):
	    image = file("./pic/{}".format(name))
	    resp = Response(image, mimetype="image/jpeg")
	    return resp

@app.route('/image_upload',methods=['GET','POST'])
def uploadImage():
	content = request.values.get("message")
	qq = int(request.values.get("account"))
	image_files = []
	for key in request.files.keys():
	    image_files.append(request.files.get(key))
	image_URL = []
	image_path = []
        for file in image_files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		image_path.append(os.path.join(app.config['UPLOAD_FOLDER'],filename))
		score = get_nsfw_score(input_file=image_path[-1])
		print "detect result: " + str(score)
                image_URL.append(os.path.join(app.config['UPLOAD_URL_PREFIX'] + str(app.config['PORT'])+"/pic/", filename))
	#tag_id = getAITagId(image_files)
	momentpath = '/home/ubuntu/ToYou/toyou/tuyouAlgorithm/picture/moment/'
	moment_list = os.listdir(momentpath)
	image_class = []
	for path in image_path:	
		image_class.append(getimageclassMap(path,allclassmean))
		print "image_class:", image_class[-1]
        if len(image_class) > 0:
		tag_id = int(image_class[0]) 
	else:
		return jsonify(result = False, error = ' there is no pictures')
	print "tag_id: "+str(tag_id)
	message_id = addPostByQq(qq,content,tag_id,image_URL)	
	print message_id
	return jsonify(result='true',tag_id=tag_id,message_id = message_id)

@app.route('/new_message_upload',methods=['GET','POST'])
def uploadMessage():
	postid =  request.values.get('message_id')
	tag = request.values.get('tag')
	post = Post.query.filter_by(id=postid).first()
	post.tag = int(tag)
	db.session.commit()
        return jsonify(result='true')

@app.route('/own_message',methods=['GET','POST'])
def getOwnMessage():
	if request.method == "POST":
		qq =  int(request.form.get('account'))
	if request.method == "GET":
		qq = int(request.args.get('account'))
	qq = int(request.values.get('account'))
	user = User.query.filter_by(qq=qq).first()
	if user == None:
		return jsonify({'state':201,'error':'the user not found!'})
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
            	'username': User.query.filter_by(id=post.userid).first().username, \
		'account': User.query.filter_by(id=post.userid).first().qq, \
		'likecount':likecount[int(post.id)], \
		'commentcount':commentcount[int(post.id)] \
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
	result.reverse()
    	return jsonify({'state': 200, 'error': '', 'data': result})

