import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 计算直方图函数
def histCover(img):
    equ = cv.equalizeHist(img)

    cv.imshow("src", img)
    cv.imshow("result", equ)
    
    cv.waitKey(0)
    cv.imwrite("../result/A/equ_contrast.jpg", np.hstack((img, equ)))

    # 均衡化后直方图计算，显示均衡化对比效果
    plt.figure("对比图", figsize=(8, 4))
    plt.subplot(121)
    plt.hist(img.ravel(), 256)
    plt.subplot(122)
    plt.hist(equ.ravel(), 256)
    plt.xlim([0, 255])
    plt.savefig("../result/A/histogram_contrast.jpg")
    plt.show()
    
    