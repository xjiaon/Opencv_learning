import cv2

cap=cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH,1080)
#cap.set(4,720)
#cap.set(15, 2.0)
#cap.set(5,30)
#cap.set(15,1)
#cap.set(14,131)

cap.set(10,250)#亮度，最高250
cap.set(11,250)#对比度，最高250
cap.set(15,2)#曝光时间，最高0，普通-4
for i in range(0,37):
    print (i,cap.get(23))
#print (cap.get(3))
while True:
    print (cap.get(10),cap.get(11),cap.get(12),cap.get(13),cap.get(14),cap.get(15))
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,6)
    cv2.imshow('gray+',gray+gray+gray+gray)
    cv2.imshow('1',frame)
    cn=cv2.waitKey(1)
    if cn==ord('q'):
        print ('q')
        break
    elif cn==ord('s'):
        print ('s')
        cv2.imwrite('1.png',frame)
cv2.destroyAllWindows()
cap.release()
