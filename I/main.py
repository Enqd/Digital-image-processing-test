import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 读取灰度图片
img = cv.imread('../img/imgae1.jpg', 0)

#laplacian_rgb = cv.Laplacian(dft_shift, cv.CV_64F)

# 空间域拉普拉斯算子
laplacian_kernel = np.array([[0, 1, 0],
                              [1, -4, 1],
                              [0, 1, 0]])
laplacian_space = cv.filter2D(img, -1, laplacian_kernel)

# 频率域拉普拉斯算子
# 将图像转换到频域
dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# 生成拉普拉斯算子的频率响应
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2
laplacian_freq = np.zeros((rows, cols, 2), np.float32)

# 拉普拉斯算子的频率响应
for i in range(rows):
    for j in range(cols):
        D = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
        laplacian_freq[i, j] = -D**2

# 应用频率域拉普拉斯算子
filtered_dft = dft_shift * laplacian_freq
f_ishift = np.fft.ifftshift(filtered_dft)
img_back_freq = cv.idft(f_ishift)
img_back_freq = cv.magnitude(img_back_freq[:, :, 0], img_back_freq[:, :, 1])

# 显示结果
plt.figure(figsize=(12, 10))
plt.subplot(1, 3, 1), plt.imshow(img, cmap='gray'), plt.title('Original Image'), plt.axis('off')
plt.subplot(1, 3, 2), plt.imshow(laplacian_space, cmap='gray'), plt.title('Laplacian (Spatial Domain)'), plt.axis('off')
plt.subplot(1, 3, 3), plt.imshow(img_back_freq, cmap='gray'), plt.title('Laplacian (Frequency Domain)'), plt.axis('off')

plt.savefig('../result/I/result.jpg')
plt.show()
