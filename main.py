import cv2 as cv
import numpy as np

cap = cv.VideoCapture("assets/FRC_2026_shooter_test.mp4")
fps = 30 
delay = int(1000 / fps)
# todo add mp4 video of frc game pieces 

while(1):

    k = cv.waitKey(delay) & 0xFF

    if k == 27:
        break
    # Take each frame
    ret, frame = cap.read()
    if not ret or frame is None:
        print("Error: Frame is empty. Check camera connection or video file.")
        cap = cv.VideoCapture("assets/FRC_2026_shooter_test.mp4")
        continue;
    frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of desired color in HSV
    #### for chem class thingy
    #lower_cl = np.array([15,100,100])
    #upper_cl = np.array([25,255,255])


    ##### for earpod thing
    lower_cl = np.array([20,230,160])
    upper_cl = np.array([28,255,255])

    # Threshold the HSV image to get only desired colors
    mask = cv.inRange(hsv, lower_cl, upper_cl)
    

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    
    edges = cv.Canny(mask,0,0)

    # Find contours
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    for i, contour in enumerate(contours ):
        
        area = cv.contourArea(contour)

        if area < 100:
            continue
        
        perimeter = cv.arcLength(contour, True)
        if perimeter == 0:
            continue

        # is sort of like a circle 
        circularity = (4 * np.pi * area) / (perimeter**2)

        if circularity < 0.3:
            continue


        ((x, y), radius) = cv.minEnclosingCircle(contour)
        center = (int(x), int(y))
        cv.circle(frame, center, int(radius), (0, 255, 0), 2)



    cv.imshow('frame',frame)
    #cv.imshow('mask',mask)
    #cv.imshow('res',res)

cv.destroyAllWindows()
