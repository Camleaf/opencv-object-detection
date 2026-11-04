import cv2 as cv
import numpy as np

cap = cv.VideoCapture("assets/FRC_2026_shooter_test.mp4")

# todo add mp4 video of frc game pieces 

while(1):

    k = cv.waitKey(10) & 0xFF

    if k == 27:
        break
    # Take each frame
    ret, frame = cap.read()
    if not ret or frame is None:
        print("Error: Frame is empty. Check camera connection or video file.")
        cap = cv.VideoCapture("assets/FRC_2026_shooter_test.mp4")
        continue;
    frame = cv.resize(frame, (0, 0), fx=0.75, fy=0.75, interpolation=cv.INTER_AREA)
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of desired color in HSV
    lower_cl = np.array([20,200,0])
    upper_cl = np.array([30,255,255])

    # Threshold the HSV image to get only desired colors
    mask = cv.inRange(hsv, lower_cl, upper_cl)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)

    edges = cv.Canny(res,0,100)

    cv.imshow('edges',edges)

    #cv.imshow('frame',frame)
    #cv.imshow('mask',mask)
    #cv.imshow('res',res)

cv.destroyAllWindows()
