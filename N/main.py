import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('../img/imgae1.jpg', 0)

img = cv.Canny(img, 100, 200)

plt.title('Canny_img')
plt.axis('off')
plt.imshow(img, cmap = 'gray')
plt.savefig("../result/N/Canny.jpg", bbox_inches='tight', pad_inches=0)
plt.show()