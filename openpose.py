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

def getkeyxy(img):#获取关键节点坐标
    im = cv2.resize(img,(640,360,))#设置为固定分辨率
    datum = op.Datum()
    datum.cvInputData = im
    opWrapper.emplaceAndPop(op.VectorDatum([datum]))
    return datum.cvOutputData,datum.poseKeypoints#返回值1为骨架图，返回值2为坐标

def getkeyary(keypoint):#坐标绘图
    return 0