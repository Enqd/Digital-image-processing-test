import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('../img/imgae1.jpg', 0) # 读取灰度图片

# 将图像转换到频域
dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# 图像尺寸
rows, cols = img.shape
crow, ccol = rows // 2, cols // 2  # 中心位置

# 定义滤波器尺寸
D0 = 30  # 截止频率

# 理想低通滤波器
ILPF = np.zeros((rows, cols, 2), np.float32)
ILPF[crow-D0:crow+D0, ccol-D0:ccol+D0] = 1

# 巴特沃斯低通滤波器
n = 2  # 巴特沃斯滤波器的阶数
BLPF = np.zeros((rows, cols, 2), np.float32)
for i in range(rows):
    for j in range(cols):
        D = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
        BLPF[i, j] = 1 / (1 + (D / D0) ** (2 * n))

# 高斯低通滤波器
GLPF = np.zeros((rows, cols, 2), np.float32)
for i in range(rows):
    for j in range(cols):
        D = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
        GLPF[i, j] = np.exp(-(D ** 2) / (2 * (D0 ** 2)))

# 应用滤波器并转换回空域
filters = [("I", ILPF), ("B", BLPF), ("G", GLPF)]
results = []
for (name, filter_mask) in filters:
    # 应用滤波器
    filtered_dft = dft_shift * filter_mask
    # 逆傅里叶变换回空域
    f_ishift = np.fft.ifftshift(filtered_dft)
    img_back = cv.idft(f_ishift)
    img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    results.append((name, img_back))

# 显示结果
plt.figure()
plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.axis('off')

for i, (name, result) in enumerate(results, 2):
    plt.subplot(2, 2, i), plt.imshow(result, cmap='gray')
    plt.title(f'{name}LPF'), plt.axis('off')

plt.savefig('../result/H/result.jpg')

plt.show()