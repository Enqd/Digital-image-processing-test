import cv2 as cv
import numpy as np

def boxFilter(img, fileName):
    # 方框滤波,normalize为True时，方框滤波就是均值滤波
    blur = cv.boxFilter(img, -1, (3, 3), normalize=False)
    cv.imshow('BoxFilter', np.hstack((img, blur)))
    cv.imwrite(fileName, np.hstack((img, blur)))
    cv.waitKey(0)