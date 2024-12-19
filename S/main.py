import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 读取灰度图像
image = cv.imread('../img/imgae1.jpg', cv.IMREAD_GRAYSCALE)  # 替换为你的图像路径

# 应用高斯滤波，减少噪声
blurred_image = cv.GaussianBlur(image, (5, 5), 0)

# 应用Canny边缘检测
edges = cv.Canny(blurred_image, 50, 150, apertureSize=3)

# 使用Hough Line Transform检测直线
# 参数解释：
# edges: 边缘检测后的图像
# rho: 极坐标的距离分辨率（像素级）
# theta: 极坐标的角度分辨率（弧度）
# threshold: 最小投票数（直线被检测的阈值）
lines = cv.HoughLines(edges, rho=1, theta=np.pi / 180, threshold=170)

# 在原图上绘制检测到的直线
output = cv.cvtColor(image, cv.COLOR_GRAY2BGR)  # 转换为BGR图像便于绘制彩色直线
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv.line(output, (x1, y1), (x2, y2), (55, 100, 195), 2)

# 显示结果
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.imshow(edges, cmap='gray')
plt.title('Canny Edges')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv.cvtColor(output, cv.COLOR_BGR2RGB))
plt.title('Hough Line Transform')
plt.axis('off')

plt.tight_layout()
plt.savefig('../result/S/res.jpg', bbox_inches='tight', pad_inches=0)
plt.show()
