import numpy as np
import cv2
import copy
import DTW as dtw

#处理流程：
#keychange()对两video对象进行压缩
#align()对齐
#get_twf()返回积累矩阵，矩阵最后一个函数即为积累距离

#返回两点距离
def get_distance(a,b):
    return pow(pow(b[0] - a[0],2) + pow(b[1] - a[1],2),1/2)

#压缩并求相对坐标，处理对象video
def keychange(ary):
    ans = ary[:,[0,1,2,3,4,5,6,7,15,16,17,18],:]
    for j in ans:
        center = copy.deepcopy(j[0])
        for i in j:
            i[0] = i[0] - center[0]
            i[1] = i[1] - center[1]
    return ans

#将ary2向ary1等比例对齐，处理对象video
def align(ary1,ary3):
    proportion = get_distance(ary1[0,0],ary1[0,1]) / get_distance(ary3[0,0],ary3[0,1])
    ary3 *= proportion
    return ary3

#基于欧式距离获取两个单帧的相似度，处理对象frame,要求为相对坐标并已经对齐
def get_Ed(ary1,ary2):
    sum = 0
    #for i in range(ary1.shape[0]):
    for i in range(2,9):
        sum += get_distance(ary1[i],ary2[i])
    return pow(sum,1/2)
        
def get_twf(A,B,dis_fuc = get_Ed):#计算两个视频序列的累计距离
    N_A = len(A)
    N_B = len(B)
    D = np.zeros([N_A,N_B])
    D[0,0] = dis_fuc(A[0],B[0])
    for i in range(1,N_A):
        D[i,0] = D[i - 1,0] + dis_fuc(A[i],B[0])
    for j in range(1,N_B):
        D[0,j] = D[0,j - 1] + dis_fuc(A[0],B[j])
    for i in range(1,N_A):
        for j in range(1,N_B):
            D[i,j] = dis_fuc(A[i],B[j]) + min(D[i - 1,j - 1],D[i - 1,j],D[i,j - 1])
    return D
    
