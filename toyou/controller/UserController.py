#coding: utf-8
import time
import random
import string
from toyou  import app ,db
from toyou.helpers.UserHelper import *
from flask import Blueprint, request, jsonify


@app.route('/login')
def login():
    userQq = request.args.get("account")
    user, _ = getUserByQq(userQq)
    tag_id_array = request.args.get("tag_id_array")
    # return tag_id_array
    if user is None:
        return jsonify(result=False)
    else:
        return jsonify(result=True)

