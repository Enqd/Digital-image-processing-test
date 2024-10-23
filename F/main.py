import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 读取输入图像
img = cv.imread('../img/imgae1.jpg')
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # 转换为RGB格式

# ----------------------- RGB空间操作 -----------------------
# 均值滤波
mean_filter_rgb = cv.blur(img_rgb, (5, 5))

# 拉普拉斯变换
# 先均值滤波，再拉普拉斯变换
laplacian_rgb = cv.Laplacian(mean_filter_rgb, cv.CV_64F)

# # ----------------------- HSI空间操作 -----------------------
# 将图像从RGB转换为HSV（HSV是HSI的近似替代）
img_hsv = cv.cvtColor(img_rgb, cv.COLOR_RGB2HSV)

# 对强度分量进行均值滤波
H, S, V = cv.split(img_hsv)

# # 将 H 和 S 转换为 float64 类型
# H = H.astype(np.float64)
# S = S.astype(np.float64)

mean_filter_V = cv.blur(V, (5, 5))

# 对均值滤波后的强度分量进行拉普拉斯变换
laplacian_V = cv.Laplacian(mean_filter_V, cv.CV_8U)

# print(np.shape(H))
# print(np.shape(S))
# print(np.shape(laplacian_V))
# print(H.dtype)
# print(S.dtype)
# print(laplacian_V.dtype)

# 将处理后的强度分量合并回HSI图像
img_hsv_filtered = cv.merge([H, S, laplacian_V])

# 将处理后的图像从HSV转换回RGB
img_hsi_filtered = cv.cvtColor(img_hsv_filtered, cv.COLOR_HSV2RGB)

# ----------------------- 结果对比 -----------------------
# 显示原始图像、RGB处理结果和HSI处理结果
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(img_rgb)
plt.title('Original RGB Image')

plt.subplot(1, 3, 2)
plt.imshow(laplacian_rgb)
plt.title('Blur and Laplacian in RGB Space')

plt.subplot(1, 3, 3)
plt.imshow(img_hsi_filtered)
plt.title('Blur and Laplacian in HSI Space')

plt.savefig("../result/F/result.jpg")
plt.show()
