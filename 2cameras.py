import cv2
import numpy as np
cap0=cv2.VideoCapture(0)
cap1=cv2.VideoCapture(1)
while(1):
    t0=cap0.grab()
    print t0
    ret0, frame0=cap0.read()
    r1=cap0.retrieve()
    
    t1=cap1.grab()
    #cv2.imshow('0',t1)
    r2=cap1.retrieve()
    ret1, frame1=cap1.read()
    print t1
    print frame0
    
    #ret1, frame1=cap1.read()
    #print frame1
    cv2.imshow('0',frame0)
    #ret1, frame1=cap1.read()
    cv2.imshow('1',frame1)
    cv2.waitKey(50)
    
    
    
