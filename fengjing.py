# -*- coding: cp936 -*-
#中文，你懂得
#!/usr/bin/python
'''
人在家中， 周游世界， 与世界各地风景名胜合影
用法如下
   
'''
import cv2
import numpy as np
import time
if __name__ == '__main__':
    
#如果是其他脚本调用，不执行下面的命令
    print(__doc__)
     #显示前面绿色的声明的内容
    print ('当前opencv版本为'+cv2.__version__)
    #显示opencv版本
    print ('你的python版本信息为')
    print (sys.version_info)
cv2.namedWindow('mix',0)

cap=cv2.VideoCapture(0)
ret = cap.set(3,1280)
ret = cap.set(4,720)
c=1
d=0
im = cv2.imread('s2.jpg')

im_white= cv2.imread('white.jpg')
while (True):
    #cv2.imshow('im_test',im)
    #cv2.waitKey(0)
    ret,frame=cap.read()
    #ren = frame[280:580, 330:430]
    #frame = cv2.rectangle(frame,(280,330),(430,580),(0,255,0),1)
    im_white[280:720, 330:730]=frame[280:720, 330:730]
    frame=im_white
    cv2.imshow('111',frame)
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

    gray = cv2.cvtColor(frame, 6)
    #cv2.imshow('gray',gray)
    a,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    #cv2.imshow('thresh',thresh)
    b,thresh_INV=cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    #cv2.imshow('thresh_INV',thresh_INV)
    dst1=cv2.add(frame,frame,mask=thresh_INV)
    #cv2.imshow('dst1',dst1)
    #dst2=cv2.add(frame,frame,mask=thresh)
    #im_dst1=cv2.bitwise_and(im,im,mask=thresh)
    #cv2.imshow('im',im)
    im_dst1=cv2.add(im,im,mask=thresh)
    #cv2.imshow('im_dst1',im_dst1)
    mixed_clone =cv2.add(im_dst1,dst1)
    cv2.imshow('mix',mixed_clone)
    if cv2.waitKey(1)==ord('0'):
        d=c+25
        print 'key 0 press'
    if c==d:
        timestr = time.strftime("%Y%m%d-%H%M%S")
        cv2.imwrite('images\pic'+timestr+'.jpg',mixed_clone)
        cv2.imshow('photo',mixed_clone)
        cv2.waitKey(2000)
        cv2.destroyWindow('photo')
    c=c+1
    print c
