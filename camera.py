import cv2
import numpy as np
def max_cap_size():
    cap.set(3,3000)
    cap.set(4,3000)
    return(int(cap.get(3)),int(cap.get(4)))

cap=cv2.VideoCapture(0)
wide,high=max_cap_size()
print (wide,high)
#cap.set(3,3000)
#cap.set(4,3000)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH,1080)
#cap.set(4,720)
#cap.set(15, 2.0)
#cap.set(5,30)
#cap.set(15,1)
#cap.set(14,131)

cap.set(10,250)#亮度，最高250
cap.set(11,250)#对比度，最高250
cap.set(15 ,2)#曝光时间，最高0，普通-4
#for i in range(0,37):
    #print (i,cap.get(23))
#print (cap.get(3))
while True:
    #print (cap.get(5),cap.get(10),cap.get(11),cap.get(12),cap.get(13),cap.get(14),cap.get(15))
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,6)
    b=np.zeros((high,wide), np.uint8)
    r=np.zeros((high,wide), np.uint8)
    #cv2.imshow('gray+',gray+gray)
    merge=cv2.merge([b,gray,r])
    #cv2.imshow('1',frame)
    cv2.imshow('merge',merge)
    cn=cv2.waitKey(1)
    if cn==ord('q'):
        print ('q')
        break
    elif cn==ord('s'):
        print ('s')
        cv2.imwrite('1.png',frame)
cv2.destroyAllWindows()
cap.release()
