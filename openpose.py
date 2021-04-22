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

def getkey(img):
    datum = op.Datum()
    datum.cvInputData = frame
    opWrapper.emplaceAndPop(op.VectorDatum([datum]))
    return datum.poseKeypoints