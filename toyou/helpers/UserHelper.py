from toyou import db
from toyou.models.User import User
from toyou.models.UserFavor import UserFavor
from toyou.models.Post import Post


def getTagList(userFavor):
    taglist = []
    if userFavor.tag0 == 1:
        taglist.append(0)
    if userFavor.tag1 == 1:
        taglist.append(1)
    if userFavor.tag2 == 1:
        taglist.append(2)
    if userFavor.tag3 == 1:
        taglist.append(3)
    if userFavor.tag4 == 1:
        taglist.append(4)
    if userFavor.tag5 == 1:
        taglist.append(5)
    if userFavor.tag6 == 1:
        taglist.append(6)
    if userFavor.tag6 == 1:
        taglist.append(6)
    if userFavor.tag7 == 1:
        taglist.append(7)
    if userFavor.tag8 == 1:
        taglist.append(8)
    if userFavor.tag9 == 1:
        taglist.append(9)
    return taglist

def getUserByName(name):
    user = User.query.filter_by(username=name).first()
    if user is None:
        return None, []
    userFavor = UserFavor.query.filter_by(userid=user.id).first()
    taglist = getTagList(userFavor)
    return user, taglist

def getUserByQq(qq):
    user = User.query.filter_by(qq=qq).first()
    if user is None:
        return None, []
    userFavor = UserFavor.query.filter_by(userid=user.id).first()
    taglist = getTagList(userFavor)
    return user, taglist

def addUser(name, qq, taglist=[]):
    user = User.query.filter_by(qq=qq).first()
    if user is not None:
        return user
    tag0 = 0
    tag1 = 0
    tag2 = 0
    tag3 = 0
    tag4 = 0
    tag5 = 0
    tag6 = 0
    tag7 = 0
    tag8 = 0
    tag9 = 0
    for i in taglist:
        if i == 0:
            tag0 = 1
        elif i == 1:
            tag1 = 1
        elif i == 2:
            tag2 = 1
        elif i == 3:
            tag3 = 1
        elif i == 4:
            tag4 = 1
        elif i == 5:
            tag5 = 1
        elif i == 6:
            tag6 = 1
        elif i == 7:
            tag7 = 1
        elif i == 8:
            tag8 = 1
        elif i == 9:
            tag9 = 1
        else:
            print "Invalid tag number"
            return None
        
    user = User(username=name, qq=qq)
    db.session.add(user)
    db.session.commit()
    userFavor = UserFavor(userid=user.id, tag0=tag0, tag1=tag1, tag2=tag2,
            tag3=tag3, tag4=tag4, tag5=tag5, tag6=tag6, tag7=tag7, tag8=tag8, tag9=tag9)
    db.session.add(userFavor)
    db.session.commit()
    return user 

def deleteUserByName(name):
    user = User.query.filter_by(username=name).first()
    if user is None:
        return
    userid = user.id
    userFavor = UserFavor.query.filter_by(userid=userid).first()
    db.session.delete(user)
    db.session.commit()
    db.session.delete(userFavor)
    db.session.commit()

def deleteUserByQq(qq):
    user = User.query.filter_by(qq=qq).first()
    if user is None:
        return
    userid = user.id
    userFavor = UserFavor.query.filter_by(userid=userid).first()
    db.session.delete(user)
    db.session.commit()
    db.session.delete(userFavor)
    db.session.commit()

def changeTagByName(name, taglist=[]):
    user, _ = getUserByName(name)
    if user is not None:
        userFavor = UserFavor.query.filter_by(userid=user.id).first()
        deleteAllTags(userFavor)
        for i in taglist:
            if i == 0:
                userFavor.tag0 = 1
            elif i == 1:
                userFavor.tag1 = 1
            elif i == 2:
                userFavor.tag2 = 1
            elif i == 3:
                userFavor.tag3 = 1
            elif i == 4:
                userFavor.tag4 = 1
            elif i == 5:
                userFavor.tag5 = 1
            elif i == 6:
                userFavor.tag6 = 1
            elif i == 7:
                userFavor.tag7 = 1
            elif i == 8:
                userFavor.tag8 = 1
            elif i == 9:
                userFavor.tag9 = 1
            else:
                print "Invalid tag number"
        db.session.commit()
        retlist = getTagList(userFavor)
        return retlist
    return []

def changeTagByQq(qq, taglist=[]):
    user = User.query.filter_by(qq=qq).first()
    if user is None:
        return None 
    retlist = changeTagByName(user.username, taglist)
    return retlist

    
def getTagByQq(qq):
    user = User.query.filter_by(qq=qq).first()
    if user is None:
        return None
    userFavor = UserFavor.query.filter_by(userid=user.id).first()
    taglist = getTagList(userFavor)
    return taglist


def deleteAllTags(userFavor):
    if userFavor is None:
        return
    userFavor.tag0 = 0
    userFavor.tag1 = 0
    userFavor.tag2 = 0
    userFavor.tag3 = 0
    userFavor.tag4 = 0
    userFavor.tag5 = 0
    userFavor.tag6 = 0
    userFavor.tag7 = 0
    userFavor.tag8 = 0
    userFavor.tag9 = 0

def addPostByName(name, content="", tag=0, imagelist=[]):
    user = User.query.filter_by(username=name).first()
    if user is None:
        print "user: " + name + " does not exist"
        return
    imageList = [''] * 10
    for i in xrange(len(imagelist)):
        imageList[i] = imagelist[i]

    post = Post(userid=user.id, content=content, tag=tag, image0=imageList[0],
            image1=imageList[1], image2=imageList[2], image3=imageList[3],
            image4=imageList[4], image5=imageList[5], image6=imageList[6],
            image7=imageList[7], image8=imageList[8], image9=imageList[9])
    db.session.add(post)
    db.session.commit()
    return post

def addPostByQq(qq, content="", tag=0, imagelist=[]):
    user = User.query.filter_by(qq=qq).first()
    if user is None:
        print "user: " + str(qq) + " does not exist"
        return
    imageList = [''] * 10
    for i in xrange(len(imagelist)):
        imageList[i] = imagelist[i]

    post = Post(userid=user.id, content=content, tag=tag, image0=imageList[0],
            image1=imageList[1], image2=imageList[2], image3=imageList[3],
            image4=imageList[4], image5=imageList[5], image6=imageList[6],
            image7=imageList[7], image8=imageList[8], image9=imageList[9])
    db.session.add(post)
    db.session.commit()
    return post
    
def getMaxPostId():
    maxId = db.session.query(db.func.max(Post.id)).scalar()
    return maxId

def getPostInfoById(postid):
    post = Post.query.filter_by(id=postid).first()
    if post is None:
        print "Post ID: " + str(postid) + " is invalid"
        return None, None, None, None, None, None
    imagelist = [post.image0, post.image1, post.image2, post.image3,\
                post.image4, post.image5, post.image6, post.image7, \
                post.image8, post.image9]
    return postid, post.userid, post.posttime, post.content, post.tag, imagelist

def deletePostById(postid):
    post = Post.query.filter_by(id=postid).first()
    if post is None:
        return False
    db.session.delete(post)
    db.session.commit()
    return True
