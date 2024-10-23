import cv2 as cv
import numpy as np
import math

def cv_show(name, img):
    '''
     显示图像
    '''
    cv.imshow(name, img)
    cv.waitKey()
    cv.destroyAllWindows()


def show_two_pictures(img_one, img_two):
    '''
     对比显示两张图片
    '''
    cv.imwrite("../result/A/Contrast.jpg", np.hstack((img_one, img_two)))
    cv_show("Two Pictures", np.hstack((img_one, img_two)))


def show_four_pictures(img_one, img_two, img_three, img_four):
    '''
     对比显示三张图片
    '''
    cv_show("Two Pictures", np.hstack((img_one, img_two, img_three, img_four)))
