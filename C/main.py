import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']    # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来显示负号


img_path = "../img/imgae1.jpg"
img = cv.imread(img_path, 0)
plt.figure(figsize=(18,9))
plt.subplot(131)
plt.title("1.原图")
plt.axis('off')
plt.imshow(img, cmap="gray")

# 一阶锐化处理
# Sobel算子
img_Sobelx=cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
img_Sobelx = np.uint8(np.absolute(img_Sobelx))
plt.subplot(132)
plt.title("2.Roberts锐化后")
plt.axis('off')
plt.imshow(img_Sobelx, cmap="gray")

# 二阶锐化处理
# 拉普拉斯算子
img_Laplacian = cv.Laplacian(img, cv.CV_64F)
# 转换结果为8位图像
img_Laplacian = np.uint8(np.absolute(img_Laplacian))
plt.subplot(133)
plt.title("3.Laplacian锐化后")
plt.axis('off')
plt.imshow(img_Laplacian, cmap="gray")

plt.savefig("../result/C/result.jpg")
plt.show()