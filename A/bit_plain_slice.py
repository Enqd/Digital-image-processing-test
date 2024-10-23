import numpy as np
from showA import *

def bit_plain_slice(img):
    '''
     位平面切片
    '''
    (h, w) = img.shape
    bit_mask = np.zeros((h, w, 8), dtype=np.uint8)
    for i in range(8):
        bit_mask[:, :, i] = 2**i
    result_img = np.zeros((h, w, 8), dtype=np.uint8)
    cv_show("img_origin", img)
    cv.imwrite("../result/A/img_origin.jpg", img)
    for i in range(8):
        result_img[:, :, i] = cv.bitwise_and(img, bit_mask[:, :, i])
        # 为了更加清楚要将大于零的数处理成255
        mask = result_img[:, :, i] > 0
        result_img[mask] = 255
        cv_show(str(i), result_img[:, :, i])
        cv.imwrite("../result/A//"+str(i)+".jpg", result_img[:, :, i])
