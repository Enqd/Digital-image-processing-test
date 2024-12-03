import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img = cv.imread('../img/imgae1.jpg', cv.IMREAD_GRAYSCALE)

# ----------使用Otsu方法进行二值化-----------
ret, otsu_result = cv.threshold(img, 0, 255, cv.THRESH_OTSU)

# 显示结果
plt.imshow(otsu_result, cmap='gray')
plt.title('Otsu Segmentation' + str(ret))
plt.savefig("../result/O/res1.jpg", bbox_inches='tight', pad_inches=0)



# ----------基于边缘检测和Otsu方法的分割-----------
