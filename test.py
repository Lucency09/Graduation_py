import numpy as np
import cv2
import openpose as op


img = cv2.imread('C:/Users/Lucency/Desktop/posetest.jpg')#∂¡Õº
cv2.imshow('img',img)
 
keypage,keyary = op.getkey(img)
cv2.imshow('keypoint',keypage)
cv2.waitKey(0)