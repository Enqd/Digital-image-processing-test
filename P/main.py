import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from skimage import io

# 读取图像并转换为灰度图像
img = io.imread('../img/imgae1.jpg', as_gray=True)

# 将图像展平为二维数组
img_flat = img.reshape(-1, img.shape[1])

# 标准化处理
scaler = StandardScaler()
img_scaled = scaler.fit_transform(img_flat)

# 进行PCA降维
pca = PCA(n_components=50)  # 假设选择50个主成分
img_pca = pca.fit_transform(img_scaled)

# 使用前50个主成分重构图像
img_reconstructed = pca.inverse_transform(img_pca)

# 恢复的图像重新恢复成原图的形状
img_reconstructed = scaler.inverse_transform(img_reconstructed)
img_reconstructed = img_reconstructed.reshape(img.shape)

# 显示原图和恢复图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.imshow(img, cmap='gray')
ax1.set_title('Original Image')

ax2.imshow(img_reconstructed, cmap='gray')
ax2.set_title('Reconstructed Image')

plt.savefig("../result/P/res.jpg", bbox_inches='tight', pad_inches=0)
plt.show()
