import cv2 as cv
import filter
import matplotlib.pyplot as plt
import numpy as np

img_g = cv.imread("../result/J/gaussian_noise.png", cv.IMREAD_GRAYSCALE)
img_u = cv.imread("../result/J/uniform_noise.jpg")
img_s = cv.imread("../result/J/salt_pepper_noise.jpg")

_, axe = plt.subplots(1, 2)

# 高斯噪声与清除后前后对比
axe[0].imshow(img_g, cmap='gray')
# 算数平均滤波器
img_f = filter.arithmetic_average_filter(img_g, 3, 3)
axe[1].imshow(img_f, cmap='gray')

plt.show()