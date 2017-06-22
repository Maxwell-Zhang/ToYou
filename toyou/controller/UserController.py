#coding: utf-8
import time
import random
import string
from toyou  import app ,db
#from runtob.models.User import User
#from runtob.models.UserProfile import UserProfile
#from runtob.models.UserLoginLog import UserLoginLog
#from runtob.models.UserFightPower import UserFightPower
#from runtob.common import permission
from flask import Blueprint, request, jsonify

bp = Blueprint('user', __name__)


@bp.route('/Login', methods=['GET'])
def login():
    print "yesyesyes"
    userId = request.args.get("name")
    print str(userId)
    return str(userId)+"sss"
    '''
    userId = request.form['userId']
    token = request.form['token']
    loginDateTime = request.form['loginDateTime']
    loginLocationX = request.form['loginLocationX']
    loginLocationY = request.form['loginLocationY']
    user = User.query.filter_by(id=userId).first()
    if user is None:
        user = User.query.filter_by(username=userId).first()
        if user is None:
            user = User(username=userId, token='', lastLogin=loginDateTime)
            r.set('user_id_' + str(user.id), token)
            db.session.add(user)
            db.session.commit()
            db.session.add(UserProfile(user.id))
            db.session.commit()
            db.session.add(UserFightPower(user.id))
            db.session.commit()
    else:
        rToken = r.get('user_id_' + str(userId))
        if token != rToken:
            return jsonify(
                {'state': 401, 'error': 'token error', 'data': {'loginState': 1, 'token': '', 'userId': user.id}})
    user.token = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(32))
    r.set('user_id_' + str(user.id), user.token, ex=10000000000)
    db.session.commit()
    db.session.add(UserLoginLog(user.id, loginDateTime, loginLocationX, loginLocationY))
    db.session.commit()
    return jsonify({'state': 200, 'error': '', 'data': {'loginState': 0, 'token': user.token, 'userId': user.id}}) '''

'''
@bp.route('/UpdateInformation', methods=['POST'])
#@permission
def UpdateInformation():
    userId = request.form['userId']
    gender = request.form['gender']
    nickname = request.form['nickname']
    phone = request.form['phone']
    email = request.form['email']
    avatar = request.form['avatar']
    user = UserProfile.query.get(userId)
    user.gender = {
            '0':'male',
            '1':'female',
        }.get(gender, '')
    user.phone = phone
    user.nickname = nickname
    user.email = email #todo 校验
    user.avatar = avatar
    db.session.commit()
    return jsonify({'state': 200, 'error': ''})


@bp.route('/GetInformation', methods=['POST'])
#@permission
def GetInformation():
    queryId = request.form['queryId']
    user = User.query.get(queryId)
    profile = UserProfile.query.get(queryId)
    if profile is None:
        return jsonify({'state': 404, 'error': 'invalid query userid'})
    data = {
        'nickname': profile.nickname,
        'gender': {
            'male': 0,
            'female': 1,
        }.get(profile.gender, 2),
        'phone': profile.phone,
        'email': profile.email,
        'lastLoginDateTime': time.mktime(time.strptime(str(user.lastLogin), "%Y-%m-%d %H:%M:%S")),
        'money': user.money,
        'avatar': profile.avatar

    }
    return jsonify({'state': 200, 'error': '', 'data': data})
'''

app.register_blueprint(bp, url_prefix='/User')
