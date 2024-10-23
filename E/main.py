import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("../img/imgae1.jpg") # imread读取数据颜色值不是常用的rgb，而是bgr，plt.imshow()输出的是rgb通道的图像
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# hist_img=cv.calcHist([img], [0], None, [256], [0, 256])
# plt.plot(hist_img)
# plt.show()
B, G, R = cv.split(img) # 获取RGB通道数据
EB = cv.equalizeHist(B)
EG = cv.equalizeHist(G)
ER = cv.equalizeHist(R)
equal_img = cv.merge((EB, EG, ER))  # 合并

# 显示原始图像和均衡化图像
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original RGB Image')
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.title('Histogram Equalized RGB Image')
plt.imshow(equal_img)
plt.savefig("../result/E/rgb.jpg")
plt.show()



# 将图像从RGB转换为HSV（HSV是HSI的近似替代）
img_hsv = cv.cvtColor(img, cv.COLOR_RGB2HSV)

# 分离HSV通道
h, s, v = cv.split(img_hsv)

# 对V/I（亮度/强度）通道进行直方图均衡化
v_eq = cv.equalizeHist(v)

# 合并均衡化后的通道
equal_hsv = cv.merge([h, s, v_eq])

# 将均衡化后的图像从HSV转换回RGB
equal_hsi = cv.cvtColor(equal_hsv, cv.COLOR_HSV2RGB)

# 显示原始图像和均衡化图像
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original RGB Image')
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.title('Histogram Equalized HSI Image')
plt.imshow(equal_hsi)
plt.savefig("../result/E/his.jpg")
plt.show()
