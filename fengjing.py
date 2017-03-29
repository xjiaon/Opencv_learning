# -*- coding: cp936 -*-
#中文，你懂得
#!/usr/bin/python
'''
人在家中， 周游世界， 与世界各地风景名胜合影
用法如下
#用法python pan_painting.py  你的图片 例如 python pan_painting.py  time.jpg
#此脚本是windows环境python 2.7+opencv3.2版本的， 配置见下面的链接
https://github.com/wjb711/Opencv_learning/blob/master/windows_python2.7_opencv3.2%E5%AE%89%E8%A3%85%E9%85%8D%E7%BD%AE%E6%8C%87%E5%AF%BC.txt
#需要提前安装speech模块， 安装方法pip install speech
如提示如下错误
no module named win32com.client错误解决
请下载对应pywin32插件
https://sourceforge.net/projects/pywin32/files/pywin32/
到这里下载微软tts
http://www.microsoft.com/en-us/download/confirmation.aspx?id=27224
'''


import cv2
import numpy as np
import time
import sys
#import win32com
#import speech

#加载语音模块
def nothing(x):
    pass


print(__doc__)
#显示前面绿色的声明的内容
print ('当前opencv版本为'+cv2.__version__)
#显示opencv版本
print ('你的python版本信息为')
print (sys.version_info)
#speech.say("推荐使用720p或1080p高清摄像头")

cv2.namedWindow('mix',0)

cap=cv2.VideoCapture(0)
try:
        
    ret = cap.set(3,1280)
    ret = cap.set(3,960)
    y1=1280
    x1=960

except:
    ret = cap.set(3,640)
    ret = cap.set(3,480)
    y1=640
    x1=480
try:
    fn = sys.argv[1]
    #尝试获得命令的第一个参数， 也就是图片的名字
except:
    fn = 'images/lufugong.jpg'
    print fn
    #如果找不到上面指定的图片名称， 默认名称为lufugong.jpg
#尝试用1280x960打开摄像头， 如果失败， 使用默认的640x480
print ('实际分辨率为')
print cap.get(3)
print cap.get(4)
#ret = cap.set(3,1280)
#ret = cap.set(4,720)
c=1
d=0
im = cv2.imread(fn)

im_white= cv2.imread('images/white.jpg')
im = cv2.imread(fn)
cv2.namedWindow('颜色捕捉',0)
cv2.createTrackbar('色彩最低', '颜色捕捉', 0, 180, nothing)
cv2.createTrackbar('色彩最高', '颜色捕捉', 180, 180, nothing)
cv2.createTrackbar('纯度最低', '颜色捕捉', 0, 255, nothing)
cv2.createTrackbar('纯度最高', '颜色捕捉', 255, 255, nothing)
cv2.createTrackbar('亮度最低', '颜色捕捉', 0, 255, nothing)
cv2.createTrackbar('亮度最高', '颜色捕捉', 255, 255, nothing)

while (True):

    ret,frame=cap.read()
        
    cv2.imshow('原图',frame)
    #原图
    gray = cv2.cvtColor(frame, 6)
    cv2.imshow('原图灰度',gray)
    #灰度图
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thrs1 = cv2.getTrackbarPos('色彩最低', '颜色捕捉')
    thrs2 = cv2.getTrackbarPos('色彩最高', '颜色捕捉')
    thrs3 = cv2.getTrackbarPos('纯度最低', '颜色捕捉')
    thrs4 = cv2.getTrackbarPos('纯度最高', '颜色捕捉')
    thrs5 = cv2.getTrackbarPos('亮度最低', '颜色捕捉')
    thrs6 = cv2.getTrackbarPos('亮度最高', '颜色捕捉')

    # define range of blue color in HSV
    lower_blue = np.array([thrs1,thrs3,thrs5])
    upper_blue = np.array([thrs2,thrs4,thrs6])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imshow('Video_mask',mask)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_not(frame,frame, mask= mask)
    cv2.imshow('颜色捕捉',res)

############################################################
    

    if cv2.waitKey(10)==ord('9'):

        d=c+10

        print 'key 9 press'

        #cv2.waitKey(3000)

        #timestr = time.strftime("%Y%m%d-%H%M%S")

        #cv2.waitKey(5000)

        #ret,frame=cap.read()

        #cv2.imshow('222',frame)

        #cv2.imwrite('images\pic'+timestr+'.jpg',frame)

        #cv2.imshow('111',frame)

        #cv2.waitKey(3000)

        #cv2.destroyWindow('111')

    #if c==d:

        #timestr = time.strftime("%Y%m%d-%H%M%S")

        #cv2.imwrite('images\pic'+timestr+'.jpg',frame)

    #    im=frame

    #    cv2.imshow('111',frame)

    #    cv2.waitKey(1000)

    #    cv2.destroyWindow('111')

 


    a,thresh=cv2.threshold(gray,135,255,cv2.THRESH_BINARY)
    cv2.imshow('阀值图',thresh)
    #阀值图
    thresh_INV=cv2.bitwise_not(thresh)
     
    cv2.imshow('阀值图取反',thresh_INV)
    #阀值图取反
    dst1=cv2.add(frame,frame,mask=thresh_INV)
    #dst1=cv2.add(frame,frame,mask=mask)
    cv2.imshow('原图+阀值取反',dst1)
    dst2=cv2.add(frame,frame,mask=thresh)
    cv2.imshow('原图+阀值',dst2)
    #im_dst1=cv2.bitwise_and(im,im,mask=thresh)

    im_dst1=cv2.add(im,im,mask=thresh)

    mixed_clone =cv2.add(im_dst1,dst1)

    #cv2.imshow('mix',mixed_clone)
    cv2.imshow('最终',mixed_clone)
    if cv2.waitKey(1)==ord('0'):

        d=c+20

        print 'key 0 press'

    if c==d:

        timestr = time.strftime("%Y%m%d-%H%M%S")

        cv2.imwrite('images\pic'+timestr+'.jpg',mixed_clone)

        cv2.imshow('photo',mixed_clone)

        cv2.waitKey(2000)

        cv2.destroyWindow('photo')

    c=c+1

    print c
