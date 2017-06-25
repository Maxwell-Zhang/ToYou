# -*- coding: utf-8 -*-
from picture_detection import findmoment, sentence_score, getimageclassMap
from numpy import *
import os

# Load file of mean value
allclassmean = load('allclassmean.npy')


def main():
    imagepath = 'moment/9/12275038507579478182.png'
    momentpath = 'moment/'
    moment_list = os.listdir(momentpath)
    image_class = getimageclassMap(imagepath, allclassmean)
    print "image_class: ", image_class
'''
    score_1 = findmoment(momentpath, imagepath)
    score_2 = sentence_score(momentpath, "皮肤水润")
    score = score_1 + score_2 * 0.25
    sort_ind = argsort(score)
    sort_ind = sort_ind[::-1]
    moment_score = []
    for idx in sort_ind:
        moment_score.append(moment_list[idx])
    print moment_score
'''

if __name__ == '__main__':
    main()


