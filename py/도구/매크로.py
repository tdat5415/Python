import mss
import cv2
import numpy as np
import pyautogui as pag
import time

#while True:
#    x, y = pag.position()
#    pos_str = 'X: ' + str(x) + ' Y: ' + str(y)
#    print(pos_str)







box = {'left': -718, 'top': 950, 'width': 14, 'height': 20}

for i in range(9, -1, -1):
    with mss.mss() as sct:
        image = np.array(sct.grab(box))[:, :, :3]
        cv2.imwrite('num_img/%d.jpg'%i, image)
    time.sleep(1)



#cv2.imshow('test_img', image)
