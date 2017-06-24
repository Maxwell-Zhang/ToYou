#coding: utf-8
import time
import random
import string
from toyou  import app ,db
from toyou.helpers.UserHelper import *
from flask import Blueprint, request, jsonify


@app.route('/delete_message')
def deleteMessage():
    userQq = request.args.get("account")
    messageId = request.args.get("message_ID")
    state = deletePostById(messageId)
    if state == True:
        return jsonify(result=True)
    else:
        return jsonify(result=False)
