import cv2,datetime
cap=cv2.VideoCapture(0)
last=1
while True:
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,6)

    _,thresh=cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
    _,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    sum=0
    for cnt in contours:
        sum=sum+cv2.contourArea(cnt)
    try:
        print (sum/last)
        if sum/last >3:
            now = datetime.datetime.now()
            #print ("yes")
            im_name1=(now.strftime('%Y-%m-%d_%H%M%S')+'.jpg')
        
            cv2.imwrite(im_name1,frame)
            #cv2.imshow('Photo',im_all)
            cv2.imwrite('1.png',frame)
            print ('done')
    except:
        pass
    
    last=sum
    #print (sum)
    cv2.imshow('1',frame)

    #print (thresh.size)
    cv2.waitKey(500)
