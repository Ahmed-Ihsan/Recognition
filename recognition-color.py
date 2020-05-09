import cv2
import numpy as np

def nothing(x):
    pass

img=np.zeros((100,512,3),np.uint8)
img2=np.zeros((100,512,3),np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

cv2.createTrackbar('R1','image',0,255,nothing)
cv2.createTrackbar('G1','image',0,255,nothing)
cv2.createTrackbar('B1','image',0,255,nothing)

cap = cv2.VideoCapture(0)

while(1):
    cv2.imshow('image',img)
    cv2.imshow('image',img2)
    # Take each frame
    img_w=cv2.imread("img1.png")

    # Convert BGR to HSV
    #img_w = cv2.cvtColor(img_w, cv2.COLOR_BGR2HSV)

    r=cv2.getTrackbarPos('R','image')
    g=cv2.getTrackbarPos('G','image')
    b=cv2.getTrackbarPos('B','image')
    r1=cv2.getTrackbarPos('R1','image')
    g1=cv2.getTrackbarPos('G1','image')
    b1=cv2.getTrackbarPos('B1','image')
    
    img[:]=[b,g,r]
    img2[:]=[b1,g1,r1]
    # define range of blue color in HSV
    lower_blue = np.array([b1,g1,r1])
    upper_blue = np.array([b,g,r])

    

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(img_w, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img_w,img_w, mask= mask)

    cv2.imshow('frame',img_w)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()