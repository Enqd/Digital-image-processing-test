import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

# 显示汉字用
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义坐标数字字体及大小
def label_def():
    plt.xticks(fontproperties='Times New Roman', size=8)
    plt.yticks(fontproperties='Times New Roman', size=8)
    plt.axis('off')                                     # 关坐标，可选


# 读取图片
img = cv.imread('../img/image2.png', 1)    # 读取彩色图片

if __name__ == '__main__':                                           # 运行当前函数
    hsi = cv.cvtColor(img, cv.COLOR_BGR2HSV)   # BGR到HSI的变换
    h, s, i = cv.split(hsi)                    # 获取HSI通道数据
    im_b, im_g, im_r = cv.split(img)           # 获取RGB通道数据

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