import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
img = cv.imread('../img/imgae1.jpg', cv.IMREAD_GRAYSCALE)

# ----------使用Otsu方法进行二值化-----------
ret, otsu_result = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# 显示结果
plt.imshow(otsu_result, cmap='gray')
plt.title('Otsu Segmentation')
plt.savefig("../result/O/res1.jpg", bbox_inches='tight', pad_inches=0)



# ----------基于边缘检测和Otsu方法的分割-----------
# 使用Sobel算子计算图像的梯度幅度（边缘检测）
sobel_x = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)
sobel_y = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

# 归一化梯度幅度
gradient_magnitude = cv.normalize(gradient_magnitude, None, 0, 255, cv.NORM_MINMAX)

# 设定一个阈值T，可以根据实际情况调整
T = np.percentile(gradient_magnitude, 90)  # 选择90%强度的边缘作为阈值

# 生成二值图像g_T(x, y)
_, g_T = cv.threshold(gradient_magnitude, T, 255, cv.THRESH_BINARY)

# 用g_T(x, y)作为模板，选择强边缘区域
strong_edges = (g_T == 255).astype(np.uint8)
strong_edge_pixels = img * strong_edges  # 只保留强边缘区域

# 计算仅包含强边缘像素的图像的直方图
hist = cv.calcHist([strong_edge_pixels], [0], None, [256], [0, 256])

# 使用Otsu方法对强边缘区域进行全局分割
ret, otsu_result = cv.threshold(strong_edge_pixels, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# 显示结果
plt.imshow(otsu_result, cmap='gray')
plt.title('Otsu with Strong Edges')
plt.savefig("../result/O/res2.jpg", bbox_inches='tight', pad_inches=0)

plt.figure()
plt.title("Histogram of Strong Edge Pixels")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.plot(hist)
plt.show()