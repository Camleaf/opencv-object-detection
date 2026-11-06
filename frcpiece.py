import cv2 as cv
import numpy as np
# Fuel under neutral light. Hue 0-179, saturation and value 0-255.
LOWER = np.array([18, 150, 90])
UPPER = np.array([30, 255, 255])
KERNEL = np.ones((3, 3), np.uint8)
def find_pieces(frame_bgr, min_area=50):
    hsv = cv.cvtColor(frame_bgr, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, LOWER, UPPER)
    mask = cv.morphologyEx(mask, cv.MORPH_OPEN, KERNEL)
    mask = cv.morphologyEx(mask, cv.MORPH_CLOSE, KERNEL)
    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    boxes = []
    for c in contours:
        area = cv.contourArea(c)
        x, y, w, h = cv.boundingRect(c)
        if area < min_area:
            continue  # too small: noise, or too far away to use
        if max(w / h, h / w) > 2:
            continue  # a ball is about as wide as it is tall
        if area / (w * h) < 0.5:
            continue  # a ball fills about 0.79 of its box
        boxes.append((x, y, w, h))
    return boxes



cap = cv.VideoCapture("assets/FRC_2026_shooter_test.mp4")
if not cap.isOpened():
    raise SystemExit(f"Could not open file")

fps = 30 
delay = int(1000 / fps)

while(1):

    k = cv.waitKey(delay) & 0xFF

    if k == 27:
        break
    # Take each frame
    ret, frame = cap.read()
    if not ret or frame is None:
        print("Error: Frame is empty. Check camera connection or video file.")
        cap.set(cv.CAP_PROP_POS_FRAMES, 0)  # loop the video        
        continue;

    frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)

    for box in find_pieces(frame):
        x,y,w,h = box
        cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv.imshow('frame',frame)
