import sys
import cv2
import os
from sys import platform
import argparse
import matplotlib.pyplot as plt
dir_path = 'D:/application/openpose/openpose/build/examples/tutorial_api_python'#openpose文件目录
# Change these variables to point to the correct folder (Release/x64 etc.)
sys.path.append(dir_path + '/../../python/openpose/Release');
os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + '/../../x64/Release;' +  dir_path + '/../../bin;'
import pyopenpose as op
params = dict()
params["model_folder"] = "D:/application/openpose/openpose/models"#模型文件目录
opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()
#上诉部分为调用openpose，别动


videoCapture = cv2.VideoCapture('C:/Users/Lucency/Desktop/posetest.mp4')#视频目录
fps = videoCapture.get(cv2.CAP_PROP_FPS)  
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), 
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))  
videoWriter = cv2.VideoWriter('C:/Users/Lucency/Desktop/poseput.mp4', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, size)  
success, frame = videoCapture.read()  
print('beging................................all frame ',fps * 8)
i = 1
while success:  
    datum = op.Datum()
    datum.cvInputData = frame
    opWrapper.emplaceAndPop(op.VectorDatum([datum]))
    videoWriter.write(datum.cvOutputData) #写视频帧  
    success, frame = videoCapture.read() #获取下一帧  
    print('over frame ',i,'    all ',fps * 8,'frame')
    i += 1
print('all over')