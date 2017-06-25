# -*- coding:utf-8 -*-
"""
   Step2. Extract the word feature (50 dimensional vector, each node corresponding a class)
   based on bayesian equation.
"""
from numpy import *

import pandas as pd
import pickle
import random
import jieba

idlist = [i for i in range(20247)]
path = "D://sns_images//moment//"
worddict = {}
label1 = []
label2 = []
validlist = []
wordlen = 0

for i in idlist:
    print(i)
    fp = open("D://sns_images//momentwithoutshuffle//" + str(i) + "//descrip.txt", 'r', encoding='UTF-8')
    lines = " "
    try:
        for line in fp.readlines():
            lines += line
    except:
        print(".............")
    seg_list = jieba.cut(lines)
    for word in seg_list:
        if not (word in worddict):
            worddict[word] = wordlen
            wordlen += 1

imagesample = []
textsample = []
label = []
imagesample2 = []
textsample2 = []
iii = 0
path = "D://sns_images//momentwithoutshuffle//"
puretext = []
puretext1 = []
purelabel = []
numlist = []

for i in range(20247):
    path1 = path + str(i)
    print (i)
    tempdata = [0, 0, 0]
    tempdataw = []
    tempdata2 = []
    fp = open(path1 + "//descrip.txt", 'r', encoding='UTF-8')
    lines = " "
    try:
        for line in fp.readlines():
            lines += line
    except:
        print(".............")
    seg_list = jieba.cut(lines)
    for word in seg_list:
        tempdata.append(worddict[word])
        tempdataw.append(worddict[word])
    puretext.append(tempdataw)
    tempdata3 = pd.read_csv(path + str(i) + "//sta.txt", header=None, sep=" ")
    tempdata3 = tempdata3.values
    if tempdata3.sum() > 9:
        tempdata3 = zeros((1, 50))
    purelabel.append(list(tempdata3[0, :]))
    numm = 0
    for tt in range(50):
        if tempdata3[0, tt] == 1:
            numm += 1
    temprrr = [0, 0, 0, 0]
    if numm < 4 and numm >= 1:
        temprrr[numm-1] = 1
        numlist.append(temprrr)
    elif numm >= 4:
        temprrr[3] = 1
        numlist.append(temprrr)
    else:
        numlist.append(temprrr)

no = []
print(len(label))
print(len(imagesample))
path2 = "D://tencent//miniproject//"
textsp = path2 + "textsample.txt"
fp4 = open(textsp, "w")
ranlist = []
print(".............................")
print(len(puretext1))
print(".............................")
for i in range(len(puretext1)):
    ranlist.append(i)
random.shuffle(ranlist)
for i in range(20247):
    for j in puretext[i]:
        fp4.write(str(j) + " ")
    fp4.write("\n")

purelabel = mat(purelabel)
savetxt("D://tencent//miniproject//label50.txt", purelabel)
random.seed(7)
X_train = []
max_review_length = 50
fp = open("D://tencent//miniproject//textsample.txt", 'r')

while 1:
    tempdata = []
    line = fp.readline()
    if not line:
        break
    seq = line.split(" ")
    for i in range(len(seq)-1):
        tempdata.append(int(seq[i]))
    X_train.append(tempdata)

test = []
sta = zeros((wordlen, 50))
sta2 = zeros((1, 50))
fp.close()
y_data = pd.read_table("D://tencent//miniproject//label50.txt", header=None, sep=" ")
y_data = y_data.values

for i in range(shape(X_train)[0]):
    for t in range(50):
        if y_data[i, t] == 1:
            sta2[0, t] += 1
            flag = zeros((1, 44583))
            for j in X_train[i]:
                if flag[0,int(j)] == 0:
                    sta[int(j), t] += 1
                    flag[0, int(j)] = 1

sum1 = sta.sum(axis=1)
sum2 = sta2.sum(axis=1)
for i in range(wordlen):
    for j in range(50):
        sta[i, j] = double(sta[i, j]) / sum1[i]
for j in range(50):
    sta2[0, j] = double(sta2[0, j]) / sum2
print(sum1)
weight = zeros((wordlen, 50))
for i in range(wordlen):
    for j in range(50):
        weight[i, j] = double(sta[i, j]-sta2[0, j]) / sta2[0, j]
weight = nan_to_num(weight)
save("D://tencent//miniproject//wordweight50", weight)

output = open('D://tencent//miniproject//wordindex.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(worddict, output)
