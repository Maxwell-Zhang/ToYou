# coding: utf-8 

import requests

files = {"file":open("../01.jpg",'r')}
url='111.231.110.120:5001/Zx/image_upload'
r = requests.post(url,files=files)
#print type(r)
#print r
print 'end'
