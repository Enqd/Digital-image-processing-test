import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

# 显示汉字用
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 定义显示一张图片函数
def imshow(image):
    if image.ndim == 2:
        plt.imshow(image, cmap='gray')                     # 指定为灰度图像
    else:
        plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))


# 定义坐标数字字体及大小
def label_def():
    plt.xticks(fontproperties='Times New Roman', size=8)
    plt.yticks(fontproperties='Times New Roman', size=8)
    plt.axis('off')                                     # 关坐标，可选


# 读取图片
img = cv.imread('../img/image2.png', 1)    # 读取彩色图片


# RGB到HSI的变换
def rgb2hsi(image):
    b, g, r = cv.split(image)                    # 读取通道
    r = r / 255.0                                # 归一化
    g = g / 255.0
    b = b / 255.0
    eps = 1e-6                                   # 防止除零

    img_i = (r + g + b) / 3                      # I分量

    img_h = np.zeros(r.shape, dtype=np.float32)
    img_s = np.zeros(r.shape, dtype=np.float32)
    min_rgb = np.zeros(r.shape, dtype=np.float32)
    # 获取RGB中最小值
    min_rgb = np.where((r <= g) & (r <= b), r, min_rgb)
    min_rgb = np.where((g <= r) & (g <= b), g, min_rgb)
    min_rgb = np.where((b <= g) & (b <= r), b, min_rgb)
    img_s = 1 - 3*min_rgb/(r+g+b+eps)                                            # S分量

    num = ((r-g) + (r-b))/2
    den = np.sqrt((r-g)**2 + (r-b)*(g-b))
    theta = np.arccos(num/(den+eps))
    img_h = np.where((b-g) > 0, 2*np.pi - theta, theta)                           # H分量
    img_h = np.where(img_s == 0, 0, img_h)

    img_h = img_h/(2*np.pi)                                                       # 归一化
    temp_s = img_s - np.min(img_s)
    temp_i = img_i - np.min(img_i)
    img_s = temp_s/np.max(temp_s)
    img_i = temp_i/np.max(temp_i)

    image_hsi = cv.merge([img_h, img_s, img_i])
    return img_h, img_s, img_i, image_hsi

if __name__ == '__main__':                                           # 运行当前函数
    h, s, i, hsi = rgb2hsi(img)                                 # RGB到HSI的变换

    im_b, im_g, im_r = cv.split(img)                            # 获取RGB通道数据

    plt.subplot(241), plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB)), plt.title('原始图'), label_def()
    plt.subplot(242), plt.imshow(im_r, 'gray'), plt.title('R'), label_def()
    plt.subplot(243), plt.imshow(im_g, 'gray'), plt.title('G'), label_def()
    plt.subplot(244), plt.imshow(im_b, 'gray'), plt.title('B'), label_def()

    plt.subplot(245), plt.imshow(hsi), plt.title('HSI图'), label_def()
    plt.subplot(246), plt.imshow(h, 'gray'), plt.title('H(色调)'), label_def()
    plt.subplot(247), plt.imshow(s, 'gray'), plt.title('S(饱和度)'), label_def()
    plt.subplot(248), plt.imshow(i, 'gray'), plt.title('I(亮度)'), label_def()
    plt.savefig("../result/D/result.jpg")
    plt.show()