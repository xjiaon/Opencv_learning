# -*- coding: cp936 -*-
import cv2
import numpy as np
def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('简笔画',0)
cv2.createTrackbar('阀值1', '简笔画', 0, 255, nothing)
cv2.createTrackbar('阀值2', '简笔画', 255, 255, nothing)
cv2.createTrackbar('阀值3', '简笔画', 0, 255, nothing)
cv2.createTrackbar('阀值4', '简笔画', 255, 255, nothing)
cv2.createTrackbar('阀值5', '简笔画', 0, 255, nothing)
cv2.createTrackbar('阀值6', '简笔画', 255, 255, nothing)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    thrs1 = cv2.getTrackbarPos('阀值1', '简笔画')
    thrs2 = cv2.getTrackbarPos('阀值2', '简笔画')
    thrs3 = cv2.getTrackbarPos('阀值3', '简笔画')
    thrs4 = cv2.getTrackbarPos('阀值4', '简笔画')
    thrs5 = cv2.getTrackbarPos('阀值5', '简笔画')
    thrs6 = cv2.getTrackbarPos('阀值6', '简笔画')

    # define range of blue color in HSV
    lower_blue = np.array([thrs1,thrs3,thrs5])
    upper_blue = np.array([thrs2,thrs4,thrs6])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('简笔画',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()


