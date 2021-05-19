import numpy as np
import cv2
import openpose as op
import DTW as dtw
import copy

def get_result(ary):
    result = {'Stop':0,
              'Straight':0,
              'Pull_Over':0,
              'Turn_Left':0,
              'Turn_Right':0}
    sum = 0
    for i in ary:
        sum += i['velue']
    for i in ary:
        result[i['class']] += 1 - i['velue'] / sum
    return result