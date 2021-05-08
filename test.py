import numpy as np
import cv2
import openpose as op
import DTW as dtw
import copy

ary00 = np.load('models/actor_0/Stop.npy')
ary01 = np.load('models/actor_0/Straight.npy')
ary02 = np.load('models/actor_0/Pull_Over.npy')
ary03 = np.load('models/actor_0/Turn_Left.npy')
ary04 = np.load('models/actor_0/Turn_Right.npy')

ary10 = np.load('models/actor_1/Stop.npy')
ary11 = np.load('models/actor_1/Straight.npy')
ary12 = np.load('models/actor_1/Pull_Over.npy')
ary13 = np.load('models/actor_1/Turn_Left.npy')
ary14 = np.load('models/actor_1/Turn_Right.npy')

ary20 = np.load('models/actor_2/Stop.npy')
ary21 = np.load('models/actor_2/Straight.npy')
ary22 = np.load('models/actor_2/Pull_Over.npy')
ary23 = np.load('models/actor_2/Turn_Left.npy')
ary24 = np.load('models/actor_2/Turn_Right.npy')

ary30 = np.load('models/actor_3/Stop.npy')
ary31 = np.load('models/actor_3/Straight.npy')
ary32 = np.load('models/actor_3/Pull_Over.npy')
ary33 = np.load('models/actor_3/Turn_Left.npy')
ary34 = np.load('models/actor_3/Turn_Right.npy')

ary40 = np.load('models/actor_4/Stop.npy')
ary41 = np.load('models/actor_4/Straight.npy')
ary42 = np.load('models/actor_4/Pull_Over.npy')
ary43 = np.load('models/actor_4/Turn_Left.npy')
ary44 = np.load('models/actor_4/Turn_Right.npy')




ary00 = dtw.keychange(ary00)
ary01 = dtw.keychange(ary01)
ary02 = dtw.keychange(ary02)
ary03 = dtw.keychange(ary03)
ary04 = dtw.keychange(ary04)

ary10 = dtw.keychange(ary10)
ary11 = dtw.keychange(ary11)
ary12 = dtw.keychange(ary12)
ary13 = dtw.keychange(ary13)
ary14 = dtw.keychange(ary14)

ary20 = dtw.keychange(ary20)
ary21 = dtw.keychange(ary21)
ary22 = dtw.keychange(ary22)
ary23 = dtw.keychange(ary23)
ary24 = dtw.keychange(ary24)

ary30 = dtw.keychange(ary30)
ary31 = dtw.keychange(ary31)
ary32 = dtw.keychange(ary32)
ary33 = dtw.keychange(ary33)
ary34 = dtw.keychange(ary34)

ary40 = dtw.keychange(ary40)
ary41 = dtw.keychange(ary41)
ary42 = dtw.keychange(ary42)
ary43 = dtw.keychange(ary43)
ary44 = dtw.keychange(ary44)




ary00 = dtw.align(ary00,ary00)
ary10 = dtw.align(ary00,ary10)
ary20 = dtw.align(ary00,ary20)
ary30 = dtw.align(ary00,ary30)
ary40 = dtw.align(ary00,ary40)




d1 = dtw.get_twf(ary00,ary01)
d2 = dtw.get_twf(ary00,ary02)
d3 = dtw.get_twf(ary00,ary03)
d4 = dtw.get_twf(ary00,ary04)