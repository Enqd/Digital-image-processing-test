import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 1. 读取图像
img = cv.imread('../img/imgae1.jpg', cv.IMREAD_GRAYSCALE)

# 2. Otsu方法直接分割
def otsu_thresholding(img):
    ret, otsu_result = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    return otsu_result

# 3. 基于边缘图像和Otsu的分割方法
def edge_based_otsu(img, T=0.1):
    # 计算图像的拉普拉斯边缘图像
    laplacian = cv.Laplacian(img, cv.CV_64F)
    laplacian_abs = np.abs(laplacian)

    # 对拉普拉斯图像进行阈值处理
    _, edge_mask = cv.threshold(laplacian_abs, T * np.max(laplacian_abs), 255, cv.THRESH_BINARY)

    # 创建边缘模板图像g(x, y)
    g = edge_mask / 255  # 0和1的二值图像

    # 从原图像f(x, y)中选取g(x, y)为1的像素值
    masked_img = img * g.astype(np.uint8)

    # 步骤4：仅使用g(x, y)为1的位置计算直方图
    # 计算掩膜后的直方图
    masked_hist = cv.calcHist([masked_img], [0], None, [256], [0, 256])

    # 显示直方图
    plt.figure(figsize=(6, 4))
    plt.title('Histogram of Masked img')
    plt.plot(masked_hist)
    plt.xlim([0, 256])
    plt.savefig("../result/O/Histogram.jpg", bbox_inches='tight', pad_inches=0)
    plt.show()

    # 使用OpenCV计算Otsu阈值并分割图像
    ret, otsu_result = cv.threshold(masked_img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
    return otsu_result

# 4. 显示结果
otsu_result = otsu_thresholding(img)
edge_otsu_result = edge_based_otsu(img, T=0.1)

# 显示图像和分割结果
plt.figure(figsize=(12, 6))

# 原始图像
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original img')
plt.axis('off')

# Otsu方法分割结果
plt.subplot(1, 3, 2)
plt.imshow(otsu_result, cmap='gray')
plt.title('Otsu Segmentation')
plt.axis('off')

# 边缘+Otsu方法分割结果
plt.subplot(1, 3, 3)
plt.imshow(edge_otsu_result, cmap='gray')
plt.title('Edge-based + Otsu Segmentation')
plt.axis('off')

plt.tight_layout()
plt.savefig("../result/O/res.jpg", bbox_inches='tight', pad_inches=0)
plt.show()
