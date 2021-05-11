import numpy as np
import cv2
import openpose as op
import DTW as dtw
import copy


np.set_printoptions(threshold=np.inf)

ary = np.load('models/Stop/act_1.npy')

ary = dtw.keychange(ary)
print(ary)