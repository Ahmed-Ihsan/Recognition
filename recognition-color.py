import cv2
import numpy as np

def nothing(x):
    pass

img=np.zeros((0,512,3),np.uint8)

cv2.namedWindow('image')

cv2.createTrackbar('lower-R','image',0,255,nothing)
cv2.createTrackbar('lower-G','image',0,255,nothing)
cv2.createTrackbar('lower-B','image',0,255,nothing)
cv2.createTrackbar('upper-R','image',0,255,nothing)
cv2.createTrackbar('upper-G','image',0,255,nothing)
cv2.createTrackbar('upper-B','image',0,255,nothing)



while(1):
    #cv2.imshow('image',img)
    # Take each frame
    img_w=cv2.imread("img1.png")

    # Convert BGR to HSV
    #img_w = cv2.cvtColor(img_w, cv2.COLOR_BGR2HSV)

    r=cv2.getTrackbarPos('lower-R','image')
    g=cv2.getTrackbarPos('lower-G','image')
    b=cv2.getTrackbarPos('lower-B','image')
    r1=cv2.getTrackbarPos('upper-R','image')
    g1=cv2.getTrackbarPos('upper-G','image')
    b1=cv2.getTrackbarPos('upper-B','image')
    
    # define range of blue color in HSV
    lower_color = np.array([b,g,r])
    upper_color = np.array([b1,g1,r1])

    

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(img_w, lower_color, upper_color)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img_w,img_w, mask= mask)

    cv2.imshow('frame',img_w)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
