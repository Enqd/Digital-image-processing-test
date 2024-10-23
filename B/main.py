from Blur import *
from BoxFilter import *
from GaussianBlur import *

if __name__ == '__main__':
    img_path = '../img/imgae1.jpg'
    img = cv.imread(img_path)
    # 将图片缩小，便于查看
    width, height = img.shape[:2][::-1]
    img_resize = cv.resize(img, (int(width*0.5), int(height*0.5)), interpolation=cv.INTER_CUBIC)
    # 均值滤波
    blur(img_resize, "../result/B/mean_filter.jpg")
    # 方框滤波
    boxFilter(img_resize, "../result/B/boxFilter.jpg")
    # 高斯滤波
    # 高斯滤波相比均值滤波效率要慢，但可以有效消除高斯噪声，能保留更多的图像细节，所以经常被称为最有用的滤波器。
    gaussianBlur(img_resize, "../result/B/gaussianBlur.jpg")