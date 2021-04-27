import sys
import cv2
import os
import numpy as np
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
 
def getkey(img):#获取关键节点坐标
    #旋转90度
    dst_im = cv2.flip(img, 0)  #原型：cv2.flip(src, flipCode[, dst]) → dst  flipCode表示对称轴 0：x轴  1：y轴.  -1：both
    dst_im = cv2.transpose(dst_im)
    im = cv2.resize(dst_im,(360,640))#设置为固定分辨率
    datum = op.Datum()
    #cv2.imshow('img',img)
    #cv2.imshow('dst_im',dst_im)
    #cv2.imshow('im',im)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    datum.cvInputData = im
    opWrapper.emplaceAndPop(op.VectorDatum([datum]))
    return datum.cvOutputData,datum.poseKeypoints#返回值1为骨架图，返回值2为坐标

def getkeyary(keyary):#坐标绘图
    map = np.zeros((640,360,3),np.uint8)
    font = cv2.FONT_HERSHEY_SIMPLEX
    i = 0
    for i in range(25):
        cv2.circle(map, tuple(keyary[i,:2]), 1, (255, 255, 255), -1)
    return map

def Video_processing(instr,outstr):#视频处理
    vid = cv2.VideoCapture(instr)
    print('Start processing')
    print('............................................................')
    sucess,frame = vid.read()
    keypage,keyary = getkey(frame)
    outary = keyary[:,:,:2].copy()
    i = 1
    print('Processing complete ',i)
    print('............................................................')
    while sucess:
        i += 1
        keypage,keyary = getkey(frame)
        outary = np.vstack((outary,keyary[:,:,:2]))
        print('Processing complete ',i)
        print('............................................................')
        sucess,frame = vid.read()
    np.save(outstr,outary)