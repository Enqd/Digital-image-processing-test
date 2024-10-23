from grayscale_histogram import *
from showA import *
from grayscale_slice import *
from bit_plain_slice import *

if __name__ == '__main__':
    # 图片路径
    img_path = "../img/imgae1.jpg"
    img = cv.imread(img_path, flags=0)
    # 将图片缩小，便于查看
    width, height = img.shape[:2][::-1]
    img_resize = cv.resize(img, (int(width*0.5), int(height*0.5)), interpolation=cv.INTER_CUBIC) 
    # # 灰度级切片展示两张图片对比
    # show_two_pictures(img_resize, grayscale_slice(img_resize, 100))
    # # 位平面切片展示8张位平面处理图
    # bit_plain_slice(img_resize)
    # 灰度直方图
    histCover(img_resize)

    
