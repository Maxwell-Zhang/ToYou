#coding: utf-8
import time
import random
import string
from toyou  import app ,db
from toyou.helpers.UserHelper import *
from flask import Blueprint, request, jsonify


@app.route('/add_tag')
def add_tag():
    #retlist = changeTagByQq(qq, taglist=[])    
    userQq = request.args.get("account")
    tag_array = request.args.get("tag_array")
    taglist = getTagByQq(userQq)
    if taglist is None:
        return jsonify(result="false")

    for tag in tag_array:
        if tag.isdigit():
            num = int(tag)        
            if num not in taglist:
                print tag
                taglist += [int(tag)]
    #print taglist
    retlist = changeTagByQq(userQq, taglist)
    #return jsonify(result=retlist)
    return jsonify(result='true')

@app.route('/delete_tag')
def delete_tag():
    #retlist = changeTagByQq(qq, taglist=[])    
    userQq = request.args.get("account")
    tag_array = request.args.get("tag_array")
    taglist = getTagByQq(userQq)
    taglist = set(taglist)
    if taglist is None:
        return jsonify(result="false")

    for tag in tag_array:
        if tag.isdigit():
            num = int(tag)        
            if num in taglist:
                print tag
                taglist.remove(num)
    #print taglist
    taglist = list(taglist)
    retlist = changeTagByQq(userQq, taglist)
    #return jsonify(result=retlist)
    return jsonify(result='true')
