#!/usr/bin/env python3 

import cv2

cap = cv2.VideoCapture('test.mp4')

def process_frame(img):
    img = cv2.resize(img, (1920//2, 1080//2))
    cv2.imshow('frame', img)

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        process_frame(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
