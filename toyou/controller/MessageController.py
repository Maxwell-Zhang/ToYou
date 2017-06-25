#coding: utf-8
import time
import random
import string
from toyou  import app ,db
from flask import Blueprint, request, jsonify
from toyou.helpers.UserHelper import *

@app.route('/get_new_messages', methods=['GET','POST'])
def msgUpdate():
    print "hhh"
    if request.method == "GET":
        userQq = request.args.get("account")
    if request.method == "POST":
        userQq = request.form.get("account")
    #lastMsgId = request.args.get("newest_id")
    lastMsgId = 0
    #print str(userId)
    #print str(lastMsgId)
    
    newestMsgId = getMaxPostId() 	
    user, userTagList = getUserByQq(userQq)
    print userTagList
    msgId = []
    for i in range(lastMsgId + 1, newestMsgId + 1):
        postId, userId, postTime, content, tag, imageList = getPostInfoById(i)
	print "postId: "+str(postId) + "tag: "+ str(tag)
	if tag is not None:
	    if tag in userTagList:
		msgId.append(i) 
    msgNum = str(len(msgId))
    print msgId
    result = []
    for MessageId in msgId:
    	post = Post.query.filter_by(id=MessageId).first()
    	if post is None and 2 < 1:
       	    return jsonify({'state': 404, 'error': 'invalid msg id'})
    	data = { \
       	    'message_id': post.id, \
            'message': post.content, \
	    'postdate': post.posttime.strftime('%Y-%m-%d'), \
            'posttime': post.posttime.strftime('%H:%M'), \
            'username': User.query.filter_by(id=post.userid).first().username, \
	    'account':User.query.filter_by(id=post.userid).first().qq, \
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
		image2.append(img)
	data['img_url'] = image2
	result.append(data)
    result.reverse()
    return jsonify({'state': 200, 'error': '', 'data': result})

