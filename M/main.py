import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("../img/imgae1.jpg", 0)

# Prewitt 边缘算子
# 水平方向
kernel_Prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
# 垂直方向
kernel_Prewitt_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])

# 卷积运算
img_Prewitt_x = cv.filter2D(img, -1, kernel_Prewitt_x)
im_Prewitt_y = cv.filter2D(img, -1, kernel_Prewitt_y)
# 在实际编程中，为了减少计算量，常用绝对值来近似梯度幅度
img_Prewitt_1 = np.uint8(cv.normalize(abs(img_Prewitt_x) + abs(im_Prewitt_y), None, 0, 255, cv.NORM_MINMAX))

# 阈值化操作
# 使用固定阈值进行二值化处理（可根据需要调整阈值）
thresh_value = 100  # 设置固定阈值，选择适当的阈值进行调试
_, img_thresholded_1 = cv.threshold(img_Prewitt_1, thresh_value, 255, cv.THRESH_BINARY)

plt.title('Prewitt_xy')
plt.imshow(img_thresholded_1, cmap='gray')
plt.axis('off')
plt.savefig("../result/M/Prewitt_xy.jpg", bbox_inches='tight', pad_inches=0)
plt.show()

# 不需要平滑处理
# 理由：图片没有明显噪声

# Prewitt 边缘算子
# 45°方向
kernel_Prewitt_45 = np.array([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]])
# 135°方向
kernel_Prewitt_135 = np.array([[1, 1, 0], [1, 0, -1], [0, -1, -1]])

# 卷积运算
img_Prewitt_45 = cv.filter2D(img, -1, kernel_Prewitt_45)
im_Prewitt_135 = cv.filter2D(img, -1, kernel_Prewitt_135)
# 在实际编程中，为了减少计算量，常用绝对值来近似梯度幅度
img_Prewitt_2 = np.uint8(cv.normalize(abs(img_Prewitt_45) + abs(im_Prewitt_135), None, 0, 255, cv.NORM_MINMAX))

# 阈值化操作
# 使用固定阈值进行二值化处理（可根据需要调整阈值）
thresh_value = 100  # 设置固定阈值，选择适当的阈值进行调试
_, img_thresholded_2 = cv.threshold(img_Prewitt_2, thresh_value, 255, cv.THRESH_BINARY)

plt.title('Prewitt_diagonal')
plt.imshow(img_thresholded_2, cmap='gray')
plt.axis('off')
plt.savefig("../result/M/Prewitt_diagonal.jpg", bbox_inches='tight', pad_inches=0)
plt.show()