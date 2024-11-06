import cv2 as cv
import filter
import matplotlib.pyplot as plt
import numpy as np

img_g = cv.imread("../result/J/gaussian_noise.jpg", 0)
img_u = cv.imread("../result/J/uniform_noise.jpg", 0)
img_s = cv.imread("../result/J/salt_pepper_noise.jpg", 0)


# 高斯噪声与清除后前后对比
_, axe = plt.subplots(1, 2)
axe[0].imshow(img_g, cmap = 'gray'), axe[0].set_title('gaussian_noise')
# 算数平均滤波器
img_f = filter.arithmetic_average_filter(img_g, 3, 3)
axe[1].imshow(img_f, cmap = 'gray'), axe[1].set_title('gaussian_noise_clear')
plt.savefig("../result/K/gaussian_noise_clear.jpg", bbox_inches='tight', pad_inches=0)
plt.show()

# 均匀噪声与清除后前后对比
_, axe = plt.subplots(1, 2)
axe[0].imshow(img_u, cmap = 'gray'), axe[0].set_title('uniform_noise')
# 几何均值滤波器
img_f = filter.Geometric_mean_filter(img_u, 3, 3)
axe[1].imshow(img_f, cmap = 'gray'), axe[1].set_title('uniform_noise_clear')
plt.savefig("../result/K/uniform_noise_clear.jpg", bbox_inches='tight', pad_inches=0)
plt.show()

# 椒盐噪声与清除后前后对比
_, axe = plt.subplots(1, 2)
axe[0].imshow(img_s, cmap = 'gray'), axe[0].set_title('salt_pepper_noise')
# 最大值滤波器
img_f = filter.maximum_filter(img_s, 3, 3)
axe[1].imshow(img_f, cmap = 'gray'), axe[1].set_title('salt_pepper_noise_clear')
plt.savefig("../result/K/salt_pepper_noise_clear.jpg", bbox_inches='tight', pad_inches=0)
plt.show()