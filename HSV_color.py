# -*- coding: cp936 -*-
#中文，你懂得
'''
此脚本是用来检测物体的HSV光学属性，如颜色亮度等信息

#此脚本是windows环境python 2.7+opencv3.2版本的， 配置见下面的链接
https://github.com/wjb711/Opencv_learning/blob/master/windows_python2.7_opencv3.2%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE%E6%8C%87%E5%AF%BC.txt
#需要提前安装speech模块， 安装方法pip install speech
其中，阀值1和2代表H色彩， 3和4代表S纯度，5和6代表V明度     
'''
import cv2
import numpy as np
import sys
def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('颜色捕捉',0)
cv2.createTrackbar('阀值1', '颜色捕捉', 0, 255, nothing)
cv2.createTrackbar('阀值2', '颜色捕捉', 255, 255, nothing)
cv2.createTrackbar('阀值3', '颜色捕捉', 0, 255, nothing)
cv2.createTrackbar('阀值4', '颜色捕捉', 255, 255, nothing)
cv2.createTrackbar('阀值5', '颜色捕捉', 0, 255, nothing)
cv2.createTrackbar('阀值6', '颜色捕捉', 255, 255, nothing)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thrs1 = cv2.getTrackbarPos('阀值1', '颜色捕捉')
    thrs2 = cv2.getTrackbarPos('阀值2', '颜色捕捉')
    thrs3 = cv2.getTrackbarPos('阀值3', '颜色捕捉')
    thrs4 = cv2.getTrackbarPos('阀值4', '颜色捕捉')
    thrs5 = cv2.getTrackbarPos('阀值5', '颜色捕捉')
    thrs6 = cv2.getTrackbarPos('阀值6', '颜色捕捉')

    # define range of blue color in HSV
    lower_blue = np.array([thrs1,thrs3,thrs5])
    upper_blue = np.array([thrs2,thrs4,thrs6])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('颜色捕捉',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()


