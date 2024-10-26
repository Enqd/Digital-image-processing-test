import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('../img/imgae1.jpg', 0) # 读取灰度图片

# ----------傅里叶变化-----------------
# 将图像数据类型转换为 float32
# cv.DFT_COMPLEX_OUTPUT 参数确保输出为双通道数组，分别表示实部和虚部
dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)

# 频谱中心化
# 将低频成分移至图像中心，便于观察。默认情况下，频域的低频部分位于四个角落，这样可以将频谱中心化，视觉上更直观。
dft_shift = np.fft.fftshift(dft)

# 计算幅度谱
# cv.magnitude 计算 dft_shift 的幅度（模）谱：通过实部和虚部，得到每个频率分量的幅度值
# np.log 进行对数变换，用 20 * log 是为了增强幅度谱的可视化效果，突出较小的频率分量
magnitude_spectrum = 20 * np.log(cv.magnitude(dft_shift[:,:,0], dft_shift[:,:,1]))

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.savefig('../result/G/dft.jpg')

plt.show()

# ----------傅里叶逆变化-----------------
# 逆中心化
dft_ishift = np.fft.ifftshift(dft_shift)
# 逆傅里叶变化
img_back = cv.idft(dft_ishift)
# 计算幅度谱
img_back = cv.magnitude(img_back[:,:,0], img_back[:,:,1])

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.savefig('../result/G/idft.jpg')

plt.show()

