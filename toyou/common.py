# coding: utf-8

import time, datetime
from functools import wraps
from flask import request, jsonify
from runtob import r


def permission(f):
    @wraps(f)
    def wrapped_function(*args, **kwargs):
        token = r.get('user_id_'+str(request.form['userId']))
        if str(request.form['token']) != token:
            return jsonify({'state':403, 'error': 'error token'})
        return f(*args, **kwargs)

    return wrapped_function


def generate_response(state, error, data=None):
    if data:
        return jsonify({'state': state, 'error': error, 'data': data})
    return jsonify({'state': state, 'error': error})


def timestamp_to_datetime(timestamp):  # Timestamp 转换为 DateTime (可能涉及时区, 统一维护)
    utc_datetime = datetime.datetime.utcfromtimestamp(int(timestamp))
    return str(utc_datetime + datetime.timedelta(hours=8))  # GMT+8


def datetime_to_timestamp(s):  # DateTime 转换为 Timestamp
    return s.total_seconds()


def get_now_date_time():
    return str(datetime.datetime.now())


datetime_format = "%Y-%m-%d %H:%M:%S"


def str_to_timestamp(s):
    return int(time.mktime(time.strptime(s, datetime_format)))


def datetime_to_str(dt):
    return dt.strftime(datetime_format)

