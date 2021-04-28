

import numpy as np
import cv2
import openpose as op
ary = np.load('pose/models/Turn_Right/test.npy')
for i in range(ary.shape[0]):
    map = op.getkeyary(ary[i,:,:])
    cv2.imshow("map",map )
    #  add below code
    cv2.waitKey(50)
cv2.destroyAllWindows()
