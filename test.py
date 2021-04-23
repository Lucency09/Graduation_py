import cv2
import openpose as op
import numpy as np
ary = np.load('pose/models/Turn_Right/test.npy')
for i in range(77):
    map = op.getkeyary(ary[i,:,:])
    cv2.imshow("map",map )
    #  add below code
    cv2.waitKey(50)
cv2.destroyAllWindows()