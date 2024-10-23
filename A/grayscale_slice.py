# 灰度级切片
def grayscale_slice(img, threshold):
    (h, w) = img.shape
    img_copy = img.copy()
    for i in range(h):
        for j in range(w):
            if img_copy[i, j] > threshold:
                img_copy[i, j] = 255
            else:
                img_copy[i, j] = 0
    return img_copy