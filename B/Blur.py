import cv2 as cv
import numpy as np

# 均值滤波
def blur(img, fileName):
    # 均值模糊
    blur = cv.blur(img, (3, 3))
    # 绘制效果对比图
    # plt.figure("均值滤波器", figsize=(8, 4))
    # plt.subplot(121)
    # plt.imshow(img)
    # plt.subplot(122)
    # plt.plot(blur)
    # plt.savefig(fileName)
    # plt.show()
    cv.imshow('Blur', np.hstack((img, blur)))
    cv.imwrite(fileName, np.hstack((img, blur)))
    cv.waitKey(0)