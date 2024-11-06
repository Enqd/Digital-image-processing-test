import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def getMotionDsf(shape, angle, dist):
    xCenter = (shape[0] - 1) / 2
    yCenter = (shape[1] - 1) / 2
    sinVal = np.sin(angle * np.pi / 180)
    cosVal = np.cos(angle * np.pi / 180)
    PSF = np.zeros(shape)  # 点扩散函数
    for i in range(dist):  # 将对应角度上motion_dis个点置成1
        xOffset = round(sinVal * i)
        yOffset = round(cosVal * i)
        PSF[int(xCenter - xOffset), int(yCenter + yOffset)] = 1
    return PSF / PSF.sum()  # 归一化

# 对图片进行运动模糊
def makeBlurred(image, PSF, eps): 
    fftImg = np.fft.fft2(image)  # 进行二维数组的傅里叶变换
    fftPSF = np.fft.fft2(PSF) + eps
    fftBlur = np.fft.ifft2(fftImg * fftPSF)
    fftBlur = np.abs(np.fft.fftshift(fftBlur))
    return fftBlur

# 维纳滤波，K=0.01
def wienerFilter(input, PSF, eps, K=0.01):  
    fftImg = np.fft.fft2(input)
    fftPSF = np.fft.fft2(PSF) + eps
    fftWiener = np.conj(fftPSF) / (np.abs(fftPSF)**2 + K)
    imgWienerFilter = np.fft.ifft2(fftImg * fftWiener)
    imgWienerFilter = np.abs(np.fft.fftshift(imgWienerFilter))
    return imgWienerFilter

def getPuv(image):
    h, w = image.shape[:2]
    hPad, wPad = h - 3, w - 3
    pxy = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    pxyPad = np.pad(pxy, ((hPad//2, hPad - hPad//2), (wPad//2, wPad - wPad//2)), mode='constant')
    fftPuv = np.fft.fft2(pxyPad)
    return fftPuv

# 约束最小乘方滤波
def CLS(image, PSF, eps, gamma=0.01):  
    fftImg = np.fft.fft2(image)
    fftPSF = np.fft.fft2(PSF)
    conj = fftPSF.conj()
    fftPuv = getPuv(image)
    # absConj = np.abs(fftPSF) ** 2
    Huv = conj / (np.abs(fftPSF)**2 + gamma * (np.abs(fftPuv)**2))
    ifftImg = np.fft.ifft2(fftImg * Huv)
    ifftShift = np.abs(np.fft.fftshift(ifftImg))
    img_blur_noisy_CLS = np.uint8(cv.normalize(np.abs(ifftShift), None, 0, 255, cv.NORM_MINMAX))  # 归一化为 [0,255]
    return img_blur_noisy_CLS

# 读取原始图像
img = cv.imread("../img/imgae1.jpg", 0)  # flags=0 读取为灰度图像
hImg, wImg = img.shape[:2]

# 带有噪声的运动模糊
PSF = getMotionDsf((hImg, wImg), 45, 100)  # 运动模糊函数
img_blur = np.abs(makeBlurred(img, PSF, 1e-6))  # 生成不含噪声的运动模糊图像

# 添加高斯噪声
scale = 0.05  # 噪声方差
noisy = img_blur.std() * np.random.normal(loc=0.0, scale=scale, size=img_blur.shape)
img_blur_noisy = img_blur + noisy  # 带有噪声的运动模糊

# 对添加噪声的模糊图像进行维纳滤波
img_blur_noisy_wiener = wienerFilter(img_blur_noisy, PSF, scale)  
# 对添加噪声的模糊图像进行约束最小乘方滤波
img_blur_noisy_CLS = CLS(img_blur_noisy, PSF, scale)

_, axe = plt.subplots(1, 3)
axe[0].imshow(img, cmap='gray'), axe[0].set_title("img_origin"), axe[0].axis('off')
axe[1].imshow(img_blur_noisy, cmap='gray'), axe[1].set_title("img_blur_noisy"), axe[1].axis('off')
axe[2].imshow(img_blur_noisy_wiener, cmap='gray'), axe[2].set_title("img_wiener"), axe[2].axis('off')
plt.savefig("../result/L/wiener_filter.jpg", bbox_inches='tight', pad_inches=0)
plt.show()

_, axe = plt.subplots(1, 3)
axe[0].imshow(img, cmap='gray'), axe[0].set_title("img_origin"), axe[0].axis('off')
axe[1].imshow(img_blur_noisy, cmap='gray'), axe[1].set_title("img_blur_noisy"), axe[1].axis('off')
axe[2].imshow(img_blur_noisy_CLS, cmap='gray'), axe[2].set_title("img_cls"), axe[2].axis('off')
plt.savefig("../result/L/cls_filter.jpg", bbox_inches='tight', pad_inches=0)
plt.show()