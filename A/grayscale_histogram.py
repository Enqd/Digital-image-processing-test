import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 计算直方图函数
def histCover(img):
    # 直方图计算
    hist = cv.calcHist([img], [0], None, [256], [0, 255])
    # 图片均衡化处理
    equ = cv.equalizeHist(img)    
    # 两张图片并排显示
    cv.imshow('equalization', np.hstack((img, equ)))
    cv.waitKey(0)
    cv.imwrite("../result/A/equ_contrast.jpg", np.hstack((img, equ)))

    # 均衡化后直方图计算，显示均衡化对比效果
    hist_equ = cv.calcHist([equ], [0], None, [256], [0, 255])
    plt.figure("对比图", figsize=(8, 4))
    plt.subplot(121)
    plt.plot(hist)
    plt.subplot(122)
    plt.plot(hist_equ)
    plt.xlim([0, 255])
    plt.savefig("../result/A/histogram_contrast.jpg")
    plt.show()