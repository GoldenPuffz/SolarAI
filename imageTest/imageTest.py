import cv2 as cv

img = cv.imread('pictures/SCELL.jpg')

cv.imshow('cell', img)

cv.waitKey(0)
#use cv.videoCapture(0) to reference webcam, 1 for the first webcam connected to computer and so on
#capture.read() breaks a video frame by frame