# -*- coding: utf-8 -*-
"""
   Step1. Compute the mean vector (centroid) of each class based on the images that
   belong to this class.
"""
from numpy import *
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input
from keras.preprocessing import image

import os

batchsize = 64
allclassmean = zeros((50, 2048))
classnum = 50

# Load ResNet50 model
model = ResNet50(weights='imagenet', include_top=False)

for j in range(classnum):
    print('the class', j)
    path = 'D:\\sns_images\\class\\' + str(j)
    for root, dir, files in os.walk(path):
        imgbatch = zeros((batchsize, 224, 224, 3))
        wordindex = 0
        num = 0
        classdata = []
        for file in files:
            try:
                img = image.load_img(path + '\\' + file, target_size=(224, 224))
                if wordindex == batchsize:
                    imgbatch = zeros((batchsize, 224, 224, 3))
                    wordindex = 0
                img = image.img_to_array(img)
                img = expand_dims(img, axis=0)
                img = preprocess_input(img)
                imgbatch[wordindex] = img
                wordindex += 1
                if wordindex == batchsize:
                    num += 1
                    print(num)
                    batchresult = model.predict(imgbatch)
                    batchmean = list(mean(batchresult, axis=0))
                    classdata.append(batchmean)
            except:
                print("iii")
        classdata = mat(classdata)
        classmean = mean(classdata, axis=0)
        allclassmean[j] = classmean[0, :]

save('D:\\tencent\\miniproject\\allclassmean', allclassmean)
