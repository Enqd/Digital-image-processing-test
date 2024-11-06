import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# 生成均匀噪声
def add_uniform_noise(image, low=-50, high=50):
    # 均匀噪声的下界，默认值为 -50，表示噪声的最小值。
    # 均匀噪声的上界，默认值为 50，表示噪声的最大值。噪声会在这个范围内随机生成并添加到图像上。
    noise = np.random.uniform(low, high, image.shape).astype(np.uint8)
    noisy_image = cv.add(image, noise)
    
    return noisy_image

# 生成与图像相同大小的高斯噪声
def add_gaussian_noise(image, mean=0, std=25):
    # 高斯噪声的均值，默认值为 0，表示噪声的中心位置。
    # 高斯噪声的标准差，默认值为 25，控制噪声的强度和扩散程度。标准差越大，噪声的波动越明显。
    noise = np.random.normal(mean, std, image.shape).astype(np.uint8)
    noisy_image = cv.add(image, noise)
    
    return noisy_image

# 生成椒盐噪声
def add_salt_pepper_noise(image, salt_prob=0.01, pepper_prob=0.01):
    # 图像中“盐”噪声（白点）的出现概率，默认值为 0.01，表示在每个像素位置有 1% 的概率被替换为白色。
    # 图像中“胡椒”噪声（黑点）的出现概率，默认值为 0.01，表示在每个像素位置有 1% 的概率被替换为黑色。
    noisy_image = image.copy() # 保存副本，避免直接修改图片

    # 添加盐噪声 (白色点)
    num_salt = int(salt_prob * image.size)
    coords = [np.random.randint(0, i - 1, num_salt) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 255
    
    # 添加胡椒噪声 (黑色点)
    num_pepper = int(pepper_prob * image.size)
    coords = [np.random.randint(0, i - 1, num_pepper) for i in image.shape]
    noisy_image[coords[0], coords[1]] = 0
    
    return noisy_image

img = cv.imread('../img/imgae1.jpg', 0)

# 添加均匀噪声
uniform_noise_img = add_uniform_noise(img)
# 添加高斯噪声
gaussian_noise_img = add_gaussian_noise(img)
# 添加椒盐噪声
salt_pepper_noise_img = add_salt_pepper_noise(img)

# 显示图片
plt.figure("uniform_noise")
plt.imshow(uniform_noise_img, "gray"), plt.title('uniform_noise')
plt.savefig('../result/J/uniform_noise.jpg')

plt.figure("gaussian_noise")
plt.imshow(gaussian_noise_img, "gray"), plt.title('gaussian_noise')
plt.savefig('../result/J/gaussian_noise.jpg')

plt.figure("salt_pepper_noise")
plt.imshow(salt_pepper_noise_img, "gray"), plt.title('salt_pepper_noise')
plt.savefig('../result/J/salt_pepper_noise.jpg')

plt.show()


_, axe = plt.subplots(2, 4, figsize = (15, 8)) # _表示忽略返回值

# 绘制原图以及其灰度图
axe[0, 0].imshow(img, cmap = 'gray'), axe[0, 0].set_title('origin')
axe[0, 1].hist(img.ravel(), 256, [0, 256]), axe[0, 1].set_title('origin_hist')

# 绘制高斯噪声以及其灰度图
axe[0, 2].imshow(gaussian_noise_img, cmap = 'gray'), axe[0, 2].set_title('gaussian_noise')
axe[0, 3].hist(gaussian_noise_img.ravel(), 256, [0, 256]), axe[0, 3].set_title('gaussian_noise_hist'), axe[0, 3].set_ylim(0, 5000)

# 绘制均匀噪声以及其灰度图
axe[1, 0].imshow(uniform_noise_img, cmap = 'gray'), axe[1, 0].set_title('uniform_noise')
axe[1, 1].hist(uniform_noise_img.ravel(), 256, [0, 256]), axe[1, 1].set_title('uniform_noise_hist'), axe[1, 1].set_ylim(0, 5000)

# 绘制椒盐噪声以及其灰度图
axe[1, 2].imshow(salt_pepper_noise_img, cmap = 'gray'), axe[1, 2].set_title('salt_pepper_noise')
axe[1, 3].hist(salt_pepper_noise_img.ravel(), 256, [0, 256]), axe[1, 3].set_title('salt_pepper_noise_hist')

plt.savefig("../result/J/result.jpg")
plt.show()