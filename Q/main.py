import numpy as np
import matplotlib.pyplot as plt
from skimage import feature, color, io
from skimage.transform import resize

# 读取图像
image = io.imread('../img/imgae1.jpg')  

# 转换为灰度图
gray_image = color.rgb2gray(image)

# 调整图像大小以加速处理（可选）
gray_image = resize(gray_image, (256, 256))

# 提取HOG特征
fd, hog_image = feature.hog(gray_image, orientations=9, pixels_per_cell=(8, 8),
                            cells_per_block=(2, 2), visualize=True, block_norm='L2-Hys')

# 归一化HOG图像
hog_image_rescaled = np.sqrt(hog_image)

# 绘制HOG直方图
plt.figure(figsize=(12, 6))

# 原始图像和HOG图像
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Grayscale Image')

# 绘制HOG归一化后的直方图
plt.subplot(1, 2, 2)
plt.imshow(hog_image_rescaled, cmap='gray')
plt.title('HOG Features (Normalized)')

plt.tight_layout()
plt.savefig("../result/Q/res1.jpg", bbox_inches='tight', pad_inches=0)
plt.show()

# 输出HOG特征直方图
plt.figure(figsize=(8, 4))
plt.plot(fd)
plt.title('HOG Feature Histogram')
plt.xlabel('Bin Index')
plt.ylabel('Frequency')
plt.savefig('../result/Q/res2.jpg',bbox_inches='tight', pad_inches=0)
plt.show()