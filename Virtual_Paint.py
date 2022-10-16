import cv2
import numpy as np

#Read a webcam
cap = cv2.VideoCapture(0)
cap.set(3,640) #parameter id 3 = width
cap.set(4,480) #parameter id 4 = height
cap.set(10,100) #parameter id 10 = Brightness

# myColors = [[143,166,74,220,167,255],
#             [#another values from the color picker]]

myColors = [[123,166,74,220,152,255]]

#Pick colours live
def empty(a):
    pass
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640,240)

cv2.createTrackbar("Hue Min", "TrackBars",123,179,empty)
cv2.createTrackbar("Hue Max", "TrackBars",166,179,empty)
cv2.createTrackbar("Sat Min", "TrackBars",74,255,empty)
cv2.createTrackbar("Sat Max", "TrackBars",220,255,empty)
cv2.createTrackbar("Val Min", "TrackBars",152,255,empty)
cv2.createTrackbar("Val Max", "TrackBars",255,255,empty)



def findColor(img, myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    #TODO : set static mask for particular colours
    # lower = np.array(myColors[0][0:3])
    # upper = np.array(myColors[0][3:6])
    mask = cv2.inRange(imgHSV, lower, upper)
    # Mask set to track blue colour
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('Original', img)
    cv2.imshow('Mask', mask)

while True:
    _,img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    findColor(img, myColors)
    cv2.imshow('Original', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#1:55:50