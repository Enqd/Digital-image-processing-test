import cv2 as cv
import numpy as np

def gaussianBlur(img, fileName):
    # 高斯滤波
    gaussian = cv.GaussianBlur(img, (5, 5), 1)
    cv.imshow('GaussianBlur', np.hstack((img, gaussian)))
    cv.imwrite(fileName, np.hstack((img, gaussian)))
    cv.waitKey(0)