import sys
import cv2
import os
from sys import platform
import argparse
import matplotlib.pyplot as plt
dir_path = 'D:/application/openpose/openpose/build/examples/tutorial_api_python'
# Change these variables to point to the correct folder (Release/x64 etc.)
sys.path.append(dir_path + '/../../python/openpose/Release');
os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + '/../../x64/Release;' +  dir_path + '/../../bin;'
import pyopenpose as op
params = dict()
params["model_folder"] = "D:/application/openpose/openpose/models"
opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()
#上诉部分为调用openpose，别动


imageToProcess = cv2.imread('C:/Users/Lucency/Desktop/posetest.jpg')#读图
cv2.imshow('img',imageToProcess)


datum = op.Datum()
datum.cvInputData = imageToProcess
opWrapper.emplaceAndPop(op.VectorDatum([datum]))

keypoints = datum.poseKeypoints
print(keypoints)
print("Body keypoints: \n" + str(datum.poseKeypoints))
cv2.imshow("OpenPose 1.7.0 - Tutorial Python API", datum.cvOutputData)
cv2.waitKey(0)