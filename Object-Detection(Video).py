import cv2
import time
import math


vid=cv2.VideoCapture('C:/Users/sapsl/Downloads/Whitehat jr Python/C107/Video/footvolleyball.mp4')

tracker=cv2.TrackerCSRT_create()

ret,frame=vid.read()

a = []
b = []

T1 = 530
T2 = 300

bbox=cv2.selectROI("Tracking",frame,False)

print(bbox)

tracker.init(frame,bbox)

def drawBox(img,bbox):

    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3)


def pathTrack(img,bbox):

    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    c1 = x+int(w/2)
    c2 = y+int(h/2)
    a.append(c1)
    b.append(c2)
    cv2.circle(img,(c1,c2),2,(225,0,225),3)

    dist =math.sqrt(((c1-T1)**2 + (c2-T2)**2))
    if dist <= 15:
        cv2.putText(frame,"Goal",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    for i in range(len(a)-1):
     cv2.circle(img,(a[i],b[i]),2,(225,0,225),3)
    cv2.circle(img,(T1,T2),2,(),3)

 
while True:
    ret,frame=vid.read()

    success,bbox=tracker.update(frame)

    if success:
        drawBox(frame,bbox)
        pathTrack(frame,bbox)
    else:
        cv2.putText(frame,"Lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)


    cv2.imshow('Object Detection',frame)
    if cv2.waitKey(1)==32:
        break

vid.release()
cv2.destroyAllWindows()