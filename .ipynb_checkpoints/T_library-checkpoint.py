import numpy as np
import cv2
import openpose as op
import DTW as dtw
import copy


class T_library(object):
    """description of class"""
    def __init__(self,k = 1):
        self.lib = np.array([dtw.get_videonp('models/Stop/act_0.npy'),
              dtw.get_videonp('models/Stop/act_1.npy'),
              dtw.get_videonp('models/Stop/act_2.npy'),
              dtw.get_videonp('models/Stop/act_3.npy'),
              dtw.get_videonp('models/Stop/act_4.npy'),
              dtw.get_videonp('models/Straight/act_0.npy'),
              dtw.get_videonp('models/Straight/act_1.npy'),
              dtw.get_videonp('models/Straight/act_2.npy'),
              dtw.get_videonp('models/Straight/act_3.npy'),
              dtw.get_videonp('models/Straight/act_4.npy'),
              dtw.get_videonp('models/Pull_Over/act_0.npy'),
              dtw.get_videonp('models/Pull_Over/act_1.npy'),
              dtw.get_videonp('models/Pull_Over/act_2.npy'),
              dtw.get_videonp('models/Pull_Over/act_3.npy'),
              dtw.get_videonp('models/Pull_Over/act_4.npy'),
              dtw.get_videonp('models/Turn_Left/act_0.npy'),
              dtw.get_videonp('models/Turn_Left/act_1.npy'),
              dtw.get_videonp('models/Turn_Left/act_2.npy'),
              dtw.get_videonp('models/Turn_Left/act_3.npy'),
              dtw.get_videonp('models/Turn_Left/act_4.npy'),
              dtw.get_videonp('models/Turn_Right/act_0.npy'),
              dtw.get_videonp('models/Turn_Right/act_1.npy'),
              dtw.get_videonp('models/Turn_Right/act_2.npy'),
              dtw.get_videonp('models/Turn_Right/act_3.npy'),
              dtw.get_videonp('models/Turn_Right/act_4.npy')]
              )
        self.list = np.loadtxt(open("ed30.csv","rb"),delimiter=",",skiprows=0)
        self.k = k
        
    
    def get_simsort(self,ary):
        test = np.copy(ary)
        lis = []
        for i in range(self.k):
            _,tem = dtw.get_twf(self.lib[i],test)
            lis.append({'class':'Stop','velue':tem})
            print('.................................')
            _,tem = dtw.get_twf(self.lib[i+5],test)
            lis.append({'class':'Straight','velue':tem})
            print('.................................')
            _,tem = dtw.get_twf(self.lib[i+10],test)
            lis.append({'class':'Pull_Over','velue':tem})
            print('.................................')
            _,tem = dtw.get_twf(self.lib[i+15],test)
            lis.append({'class':'Turn_Left','velue':tem})
            print('.................................')
            _,tem = dtw.get_twf(self.lib[i+20],test)
            lis.append({'class':'Turn_Left','velue':tem})
            print('.................................')
        print('all over')
        
        lis.sort(key=lambda k:k['velue'])
        return lis
    
    
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


