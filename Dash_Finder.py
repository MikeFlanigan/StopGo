import cv2
import numpy as np
import os

def nothing(x):
    pass

cap = cv2.VideoCapture('.\\Videos\\Driving_logtech2016_10_8-10_14.avi')
cv2.namedWindow('webcam')

cv2.createTrackbar('minthresh', 'webcam', 0,255, nothing)
cv2.createTrackbar('maxthresh', 'webcam', 0,255, nothing)

while True:
    _, webcam = cap.read()
##    webcam_small = cv2.resize(webcam,None,fx=.5,fy=.5,interpolation = cv2.INTER_LINEAR)
    filtered = cv2.bilateralFilter(webcam,9,75,75)
##    gray = cv2.cvtColor(webcam,cv2.COLOR_BGR2GRAY)
##    blurred = cv2.GaussianBlur(gray,(15,15),0)
    # cv2.bilateralFilter() is designed to keep edges while blurring noise
    # so would be preferable but need to confirm that the processing speed
    # is adequate
    
    minthresh = cv2.getTrackbarPos('minthresh','webcam')
    maxthresh = cv2.getTrackbarPos('maxthresh','webcam')
##    edges_plain = cv2.Canny(webcam,minthresh,maxthresh)
##    edges_blurred = cv2.Canny(webcam,minthresh,maxthresh)
    edges_filtered = cv2.Canny(filtered,minthresh,maxthresh)
##    im2, contours, hierarchy = cv2.findContours(edges_blurred,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
##    print(len(contours))
##    cv2.drawContours(edges_blurred, contours, -1, (0,255,0), 3)
##    print(edges)
##    cv2.imshow('edges_plain',edges_plain)
##    cv2.imshow('edges_blurred',edges_blurred)
    cv2.imshow('edges_filtered',edges_filtered)
    cv2.imshow('webcam',webcam)
##    cv2.imshow('webcam_small',webcam_small)
##    cv2.imshow('gray',gray)
##    cv2.imshow('blurred',blurred)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
