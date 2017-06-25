# coding: UTF-8
from toyou import app
from toyou import db
from toyou.helpers.UserHelper import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

user = addUser(name='zy', qq=1234567890, taglist=[0,1,2,3,4,5,6,7,8,9])
print user

#user, taglist = getUserByName('zy')
#print user
#print taglist

#user, taglist = getUserByQq(1234567890)
#print user
#print taglist

#deleteUserByQq(1234567890)
#user, taglist = getUserByQq(1234567890)
#print user
#print taglist

#deleteUserByName('zy')
#user, taglist = getUserByName('zy')
#print user
#print taglist

#user = addUser(name='zy', qq=1234567890, taglist=[1,5,9])
#print user

#taglist = changeTagByName(name='zy', taglist=[1,2,3,4])
#print taglist

taglist = changeTagByQq(qq=1234567890, taglist=[7,8,9])
print taglist

taglist = getTagByQq(1234567890)
print taglist

addPostByName(name='zy', content="aaa", tag=1, imagelist=["addr1","addr2","addr3"])
addPostByQq(qq=1234567890, content="abc", tag=5, imagelist=["addr5"])
addPostByQq(qq=1234567890, content="你好啊", tag=5, imagelist=["addr5"])


maxId = getMaxPostId()
print maxId

postid, userid, posttime, content, tag, imagelist = getPostInfoById(postid=8)
print postid
print userid
print posttime
print str(unicode(content))
print tag
print imagelist

#state = deletePostById(2)
#print state

