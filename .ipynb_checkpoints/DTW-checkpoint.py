import numpy as np
import cv2
import copy
import DTW as dtw
import openpose as op

#处理流程：
#keychange()对两video对象进行压缩
#align()对齐
#get_twf()返回积累矩阵，矩阵最后一个函数即为积累距离

#video处理
def get_videonp(str):
    ary = np.load(str)
    ary = dtw.keychange(ary)
    ary = dtw.align(ary)
    return ary

#返回两点距离
def get_distance(a,b):
    return pow(pow(b[0] - a[0],2) + pow(b[1] - a[1],2),1/2)

#骨骼图播放
def keyplay(ary):
    tem = copy.deepcopy(ary)
    tem[:,:,0] += 200
    tem[:,:,1] += 180
    '''
    for j in range(ary.shape[0]):
        tem[j,2:8,0] += tem[j,1,0]
        tem[j,2:8,1] += tem[j,1,1]
    '''
    for i in tem:
        map = op.getkeyary(i)
        cv2.imshow('keyplay',map)
        cv2.waitKey(40)
    cv2.destroyAllWindows()
    
#删除错误帧
def de_error(ary):
    ans = np.copy(ary[0:1])
    for i in range(1,ary.shape[0]):
        if(detect(ary[i-1:i])):
            ans = np.vstack((ans,np.copy(ary[i-1:i])))
    return ans
    
#判断该帧是否有误
def detect(ary):
    for i in ary[0]:
        if(i[0] == 0 or i[1] == 0):
            return False
    return True
    
#压缩并求相对坐标，处理对象video
def keychange(ary):
    ans = copy.deepcopy(ary[:,[0,1,2,3,4,5,6,7,15,16,17,18],:])
    #ans = de_error(ans)
    for j in ans:
        center = copy.deepcopy(j[0])
        for i in j:
            i[0] = i[0] - center[0]
            i[1] = i[1] - center[1]
        '''
        for k in range(2,8):
            j[k,0] = j[k,0] - j[1,0]
            j[k,1] = j[k,1] - j[1,1]
        '''
    return ans

#将ary2向0、1两点距离70像素等比例对齐，处理对象video
def align(ary3):
    proportion = 70 / get_distance(ary3[0,0],ary3[0,1])
    ary3 *= proportion
    return ary3





#基于欧式距离获取两个单帧的相似度，处理对象frame,要求为相对坐标并已经对齐
#未知原理公式0.5，效果很好
def get_Ed05(ary1,ary2):
    sum = 0
    denominator = get_Denominator(ary1,ary2)
    #for i in range(ary1.shape[0]):
    for i in range(2,12):
        #dest = get_distance(ary1[i],ary1[0]) + get_distance(ary2[i],ary2[0])
        dest = get_distance(ary1[i],ary2[i])
        weight = dest / denominator
        #sum += get_distance(ary1[i],ary2[i]) * weight
        sum += dest * weight
    return pow(sum,1/2)

#带权公式1.0，效果没有0.5好，讲得通道理
#获取权值分母
def get_Denominator(ary1,ary2):
    sum = 0
    for i in ary1:
        sum += get_distance(i,ary1[0])
    for i in ary2:
        sum += get_distance(i,ary2[0])
    return sum

def get_Ed10(ary1,ary2):
    sum = 0
    denominator = get_Denominator(ary1,ary2)
    #for i in range(ary1.shape[0]):
    for i in range(2,12):
        dest = get_distance(ary1[i],ary1[0]) + get_distance(ary2[i],ary2[0])
        #dest = get_distance(ary1[i],ary2[i])
        weight = dest / denominator
        sum += get_distance(ary1[i],ary2[i]) * weight
        #sum += dest * weight
    return pow(sum,1/2)

#带权公式2.0,结合余弦相似度
def get_chcos(ary1,ary2):
    tem1 = ary1[0] * ary2[0] + ary1[1] * ary2[1]
    tem2 = pow(pow(ary1[0],2) + pow(ary1[1],2),1 / 2) * pow(pow(ary2[0],2) + pow(ary2[1],2),1 / 2)
    if(tem2 == 0):
        return 0
    return 1 - tem1 / tem2

def get_Ed20(ary1,ary2):
    sum = 0
    for i in range(2,12):
        weight = get_chcos(ary1[i],ary2[i])
        sum += get_distance(ary1[i],ary2[i]) * weight
    return pow(sum,1/2)

#带权公式3.0,结合余弦相似度
def get_Ed30(ary1,ary2):
    sum = 0
    denominator = get_Denominator(ary1,ary2)
    for i in range(2,12):
        dest = get_distance(ary1[i],ary1[0]) + get_distance(ary2[i],ary2[0])
        weight = get_chcos(ary1[i],ary2[i]) * dest / denominator
        sum += get_distance(ary1[i],ary2[i]) * weight
    return pow(sum,1/2)

#计算两个视频序列的累计距离
def get_twf(A,B,dis_fuc = get_Ed30):
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
    return D,D[D.shape[0]-1,D.shape[1]-1]
    

