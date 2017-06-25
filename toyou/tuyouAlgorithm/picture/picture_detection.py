# -*- coding: utf-8 -*-
"""
   Step3. Get image class and do recommendation based on input image
"""
from numpy import *
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input
from keras.preprocessing import image

import os
import pickle
import jieba

# Load ResNet50 model
model = ResNet50(weights='imagenet', include_top=False)

# Load file of mean value
allclassmean = load('/home/ubuntu/ToYou/toyou/tuyouAlgorithm/picture/allclassmean.npy')

map = {}
map_file = open('/home/ubuntu/ToYou/toyou/tuyouAlgorithm/picture/map.txt', 'rb')
for ele in map_file:
    attr = ele.strip().split(":")
    key = int(attr[0].strip())
    value = attr[1].strip()
    value = value[:len(value)-1]
    map[key] = value
map_file.close()


def getimageclass(imagepath, allclassmean, classnum):
    """ Input an image (path), a mean file that contains mean vectors of all class, and the class number, return
      the class of image """
    img = image.load_img(imagepath, target_size=(224, 224))
    img = image.img_to_array(img)
    img = expand_dims(img, axis=0)
    img = preprocess_input(img)
    # substitute the mean vector of the model
    feature = model.predict(img)
    # extract the feature
    feature = reshape(feature, [1, 2048])
    feature = tile(feature, (classnum, 1))
    diff = feature - allclassmean
    squarediff = multiply(diff, diff)
    euclidean = mean(squarediff, axis=1)
    realclass = argmin(list(euclidean))
    # get the class whose mean feature has min l2 distance with the feature of input image
    return realclass


def getimageclassMap(imagepath, allclassmean):
    rc = getimageclass(imagepath, allclassmean, 50)
    return map[int(rc)]

def getmomentclass(momentpath):
    """ Input the momentpath, return image class of each moment in momentclass """
    momentlist = os.listdir(momentpath)
    momentclass = dict()
    for moment in momentlist:
        moment_img_list = os.listdir(momentpath + '/' + moment)
        moment_class = zeros((len(moment_img_list) - 7,), dtype=int)
        idx = 0
        for moment_img in moment_img_list:
            if moment_img[-3:] == 'jpg' or moment_img[-3:] == 'png' or moment_img[-4:] == 'jpeg':
                moment_path = momentpath + '/' + moment + '/' + moment_img
                moment_img_class = getimageclass(moment_path, allclassmean, 50)
                moment_class[idx] = moment_img_class
                idx += 1
        momentclass[moment] = moment_class
    return momentclass


def findmoment(momentpath, imagepath):
    """ Input momentpath and imagepath, return the score of image to the momentfile """
    img_class = getimageclass(imagepath, allclassmean, 50)
    momentlist = os.listdir(momentpath)
    score = zeros(shape(momentlist))
    idx = 0
    for moment in momentlist:
        moment_img_list = os.listdir(momentpath + '/' + moment)
        moment_class_list = zeros((50,), dtype=int)
        for moment_img in moment_img_list:
            if moment_img[-3:] == 'jpg' or moment_img[-3:] == 'png' or moment_img[-4:] == 'jpeg':
                moment_path = momentpath + '/' + moment + '/' + moment_img
                # moment_img_ = image.load_img(moment_path)
                moment_class = getimageclass(moment_path, allclassmean, 50)
                moment_class_list[moment_class] += 1
        if moment_class_list[img_class] == 0:
            score[idx] = 0
        else:
            score[idx] = moment_class_list[img_class] / float(len(momentlist))
        idx += 1
    return score


def findmoment_2(momentclass, imagepath, momentpath):
    """ This function is used for return score with existing momentclass """
    img_class = getimageclass(imagepath, allclassmean, 50)
    momentlist = os.listdir(momentpath)
    score = zeros(shape(momentlist))
    idx = 0
    for moment in momentlist:
        moment_class_list = zeros((50,), dtype=int)
        print momentclass[moment]
        for moment_class in momentclass[moment]:
            print moment_class
            moment_class_list[int(moment_class)] = moment_class[moment_class] + 1
            if moment_class_list[img_class] == 0:
                score[idx] = 0
            else:
                score[idx] = moment_class_list[img_class] / float(len(momentlist))
        idx += 1
    return momentlist[argmax(score)]


def getsenfeature(sen,worddict,wordweight):
    """ Generate word feature """
    seg_list = jieba.cut(sen)
    featurelist = []
    for word in seg_list:
        if word in worddict:
            featurelist.append(wordweight[worddict[word]])
    if len(featurelist) == 0:
        return [0] * 50
    else:
        featurelist = mat(featurelist)
        feature = mean(featurelist, axis=0)
        return feature


def sentence_score(momentpath, sentence):
    """ Input momentpath and related sentence, return the score of sentence """
    worddict = pickle.load(open('wordindex_2.pkl', 'rb'))
    wordweight = load('wordweight50.npy')
    momentlist = os.listdir(momentpath)
    score = zeros(shape(momentlist))
    feature = getsenfeature(sentence, worddict, wordweight)
    idx = 0
    for moment in momentlist:
        moment_file_list = os.listdir(momentpath + '/' + moment)
        for moment_file in moment_file_list:
            if moment_file == 'descrip.txt':
                f = open(momentpath + '/' + moment + '/' + moment_file)
                f_ = f.readlines()
                moment_sentence = ''
                for line in f_:
                    moment_sentence += line
                moment_sentence_feature = getsenfeature(moment_sentence, worddict, wordweight)
                diff = moment_sentence_feature - feature
                squarediff = multiply(diff, diff)
                euclidean = mean(squarediff)
                score[idx] = euclidean
                idx += 1
    max_score = score[argmax(score)]
    score /= max_score
    return score
