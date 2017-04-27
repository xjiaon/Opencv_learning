import cv2
import numpy as np
cap=cv2.VideoCapture(0)

while cv2.waitKey(1)!=27:
    ret, frame=cap.read()
    if cv2.waitKey(1)==ord(' '):
        (x1,y1,x2,y2)=cv2.selectROI('frame',frame,0,0)
        x1=int(x1)
        x2=int(x2)
        y1=int(y1)
        y2=int(y2)
        src=frame[y1:y1+y2,x1:x1+x2]
        im=cv2.resize(src, (640, 480), interpolation = cv2.INTER_CUBIC)
        cv2.imshow('im',im)
        cv2.waitKey(1000)
    cv2.imshow('frame',frame)
cap.release()
cv2.destroyAllWindows()
