#coding: utf-8
import time
import random
import string
from toyou  import app ,db
from toyou.models.Post import Post
from flask import Blueprint, request, jsonify



@app.route('/Get_message', methods=['GET'])
def getmessage():
    AccountId = request.args.get("account")
    MessageId = request.args.get("message_id")
    post = Post.query.filter_by(id=MessageId).first()
    if post is None:
        return jsonify({'state': 404, 'error': 'invalid msg id'})
    data = {
        'result':'success',
        'message_id': post.id,
        'message': post.content,
        'image0': post.image0,
        'image1': post.image1,
        'image2': post.image2,
        'image3': post.image3,
        'image4': post.image4,
        'image5': post.image5,
        'image6': post.image6,
        'image7': post.image7,
        'image8': post.image8,
        'image9': post.image9,
        'lastLoginDateTime': time.mktime(time.strptime(str(user.lastLogin), "%Y-%m-%d %H:%M:%S")),

    }
    return jsonify({'state': 200, 'error': '', 'data': data})
    print str(AccountId)

