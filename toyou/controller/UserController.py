#coding: utf-8
import time
import random
import string
from toyou  import app ,db
from toyou.helpers.UserHelper import *
from flask import Blueprint, request, jsonify


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        print 'GET'
        userQq = request.args.get("account")
        tag_id_array = request.args.get("tag_id_array").split(',')
        print userQq
        print type(tag_id_array)
        print tag_id_array
    elif request.method == 'POST':
        print 'POST'
        userQq = request.form.get("account")
        tag_id_array = request.form.get("tag_id_array").split(',')
        print userQq
        print type(tag_id_array)
        print tag_id_array
    user, _ = getUserByQq(userQq)
    if user is None:
        return jsonify(result=False)
    taglist = []
    for tag in tag_id_array:
        if tag.isdigit():
            num = int(tag)
            taglist += [num]
    # return tag_id_array
    print taglist
    retlist = changeTagByQq(userQq, taglist)
    return jsonify(result=True)

