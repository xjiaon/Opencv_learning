# -*- coding: cp936 -*-
from __future__ import division
import numpy as np
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
ret = cap.set(3,640)
ret = cap.set(4,480)
img1=np.zeros((480,640,3), np.uint8)
cv2.namedWindow('颜色捕捉',0)
cv2.createTrackbar('色彩最低', '颜色捕捉', 500, 2000, nothing)
#cv2.imshow('img1',img1)
#cv2.waitKey(0)
while(True):
    ret, frame = cap.read()

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    #cv2.imshow('im',gray)
    #cv2.imshow('frame',frame)
    cn=cv2.waitKey(1)
    if cn==ord('0'):
        #print '0'
        img1=frame
        
        #截取对比图1
        #cv2.imshow('raw',img1)
        #cv2.waitKey(1000)
        #cv2.destroyWindow('raw')
###
    img2=frame
        #print '9'
        

        #img1 = cv2.imread('text1.png')
        #img2 = cv2.imread('text2.png')

        # Initiate STAR detector
    thrs1 = cv2.getTrackbarPos('色彩最低', '颜色捕捉')
    orb = cv2.ORB(nfeatures=thrs1)

        # find the keypoints with ORB
        #kp = orb.detect(img,None)

        # compute the descriptors with ORB
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches=bf.match(des1,des2)

    
    per=len(matches)
    #float a
    a=round(len(matches)/thrs1*100,1)
    #print per
    #print a
    matches = sorted(matches, key = lambda x:x.distance)
    img2=cv2.drawKeypoints(img2,kp2,color=(0,0,255), flags=0)
    img1_copy=cv2.drawKeypoints(img1,kp1,color=(0,0,255), flags=0)
    
        #print kp1


        # draw only keypoints location,not size and orientation
        #img2 = cv2.drawKeypoints(img,kp,color=(0,255,0), flags=0)
        #cv2.imshow('1',im)
        #cv2.waitKey(0)
    rows1 = img1.shape[0]
    cols1 = img1.shape[1]
    rows2 = img2.shape[0]
    cols2 = img2.shape[1]
    out = np.zeros((max([rows1,rows2]),cols1+cols2,3), dtype='uint8')
    out[:rows1,:cols1] =img2
    out[:rows2,cols1:]=img1_copy
    cv2.putText(out,str(a)+'%',(50,50), 0, 2,(255,255,255),2,0)
    for mat in matches:

                # Get the matching keypoints for each of the images
        img1_idx = mat.queryIdx
        img2_idx = mat.trainIdx
        (x1,y1) = kp1[img1_idx].pt
        (x2,y2) = kp2[img2_idx].pt
            #cv2.circle(out, (x1,y1), 4, (255, 0, 0), 1) 
        cv2.circle(out, (int(x2),int(y2)), 4, (0, 255, 0), 1)
        cv2.circle(out, (int(x2+640),int(y2)), 4, (0, 255, 0), 1) 
            #print kp1[img1_idx].pt

    cv2.imshow('颜色捕捉',out)


    






















    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


