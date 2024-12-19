import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image = cv.imread('../img/imgae1.jpg', cv.IMREAD_GRAYSCALE)  # 替换为你自己的图像路径

# 进行高斯模糊，减少噪声
blurred_image = cv.GaussianBlur(image, (5, 5), 0)

# 使用Harris角点检测函数
# Harris角点检测的参数：
# image: 输入图像
# blockSize: 邻域大小（即计算梯度时的区域大小）
# ksize: Sobel算子的大小，用于计算图像梯度
# k: Harris检测的自由参数（通常设定为0.04到0.06之间）
corner_response = cv.cornerHarris(blurred_image, blockSize=2, ksize=3, k=0.04)

# 扩展角点响应，便于观察
corner_response = cv.dilate(corner_response, None)

# 在图像上标记角点，设置一个阈值
image_with_corners = np.copy(image)
image_with_corners[corner_response > 0.01 * corner_response.max()] = 255

# 显示原图和角点检测结果
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(image_with_corners, cmap='gray')
plt.title('Harris Corners Detected')
plt.axis('off')

plt.tight_layout()
plt.savefig('../result/R/res.jpg', bbox_inches='tight', pad_inches=0)
plt.show()