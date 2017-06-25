# coding: utf-8 

import requests


files = {"account":1234567890, "tag_id_array":"3,7"}
url='http://111.231.110.120:5008/login'
r = requests.post(url, data=files)
#r = requests.get(url+"?account=1234567890&tag_id_array=8,9")
#print type(r)
#print r
