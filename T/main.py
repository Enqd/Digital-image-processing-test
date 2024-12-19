import cv2 as cv
import matplotlib.pyplot as plt

# 加载预训练的人脸检测级联分类器
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 读取图像
image = cv.imread('../img/face1.jpg')  # 替换为你的图像路径
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 转换为灰度图像

# 检测人脸
# 参数解释：
# scaleFactor: 图像缩放比例，每次图像尺寸减小的比例。较大的值检测速度更快，但可能会漏检。
# minNeighbors: 每个候选矩形的最小重叠次数，较高的值减少误检，但可能漏检。
# minSize: 检测窗口的最小大小，设置为(30, 30)即可检测常见人脸。
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))

# 绘制检测到的人脸
for (x, y, w, h) in faces:
    cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# 显示结果
plt.figure(figsize=(10, 6))
plt.imshow(cv.cvtColor(image, cv.COLOR_BGR2RGB))
plt.title(f'Detected {len(faces)} Faces')
plt.axis('off')
plt.savefig('../result/T/res.jpg', bbox_inches='tight', pad_inches=0)
plt.show()
