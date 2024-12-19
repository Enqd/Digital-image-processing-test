
# Digital-image-processing-test

本项目是数字图像处理相关的实践代码仓库，涵盖了图像增强、复原、分割以及计算机视觉等多个方面的处理算法和实验。


## 目录

1. [项目概述](#%E9%A1%B9%E7%9B%AE%E6%A6%82%E8%BF%B0)
2. [功能模块](#%E5%8A%9F%E8%83%BD%E6%A8%A1%E5%9D%97)
   * [图像增强](#%E5%9B%BE%E5%83%8F%E5%A2%9E%E5%BC%BA)
   * [图像复原](#%E5%9B%BE%E5%83%8F%E5%A4%8D%E5%8E%9F)
   * [图像分割](#%E5%9B%BE%E5%83%8F%E5%88%86%E5%89%B2)
   * [计算机视觉](#%E8%AE%A1%E7%AE%97%E6%9C%BA%E8%A7%86%E8%A7%89)
3. [使用方法](#%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95)
   * [安装依赖](#%E5%AE%89%E8%A3%85%E4%BE%9D%E8%B5%96)
   * [运行代码](#%E8%BF%90%E8%A1%8C%E4%BB%A3%E7%A0%81)
   * [查看结果](#%E6%9F%A5%E7%9C%8B%E7%BB%93%E6%9E%9C)
4. [贡献指南](#%E8%B4%A1%E7%8C%AE%E6%8C%87%E5%8D%97)
5. [联系方式](#%E8%81%94%E7%B3%BB%E6%96%B9%E5%BC%8F)
6. [许可证](#%E8%AE%B8%E5%8F%AF%E8%AF%81)

## 一、项目概述

数字图像处理在众多领域有着广泛应用，如医疗影像、自动驾驶、监控系统、遥感图像等。本项目旨在通过一系列实验实现和分析不同的图像处理技术，帮助理解和掌握数字图像处理的基本原理与方法。无论您是数字图像处理的初学者，还是希望提升算法实践能力的开发者，本项目都能为您提供有价值的示例和实现。

## 二、功能模块

### （一）图像增强

1. **灰度级切片**
   * 通过设定阈值，将大于阈值的像素设为白色，小于阈值的设为黑色，突出特定灰度范围。
   * 能突出图像中如建筑物轮廓等特征，但会丢失细节和渐变，形成高对比黑白效果。
2. **位平面切片**
   * 将图像视为由多个比特平面组成，分析各比特平面对图像外观的贡献。
   * 低位平面包含噪声和不明显细节，中间位平面捕捉图像特征，高位平面保持图像主要结构信息。
3. **直方图处理**
   * 进行直方图均衡化，使图像灰度级像素分布更合理。
   * 均衡化前直方图集中，图像对比度差；均衡化后趋于平坦，对比度增强，细节更清晰。
4. **滤波与锐化**
   * 均值、方框、高斯滤波器：用于图像平滑处理，其中均值滤波器对实验图片细节保留好，高斯滤波器次之，方框滤波器最差。
   * Sobel 和 Laplacian 算子：分别实现一阶和二阶锐化，Sobel 锐化增强水平边缘，Laplacian 锐化提取更多细节，但可能引入噪声。
5. **RGB 和 HSI 空间操作**
   * RGB 和 HSI 分量图：展示图像在不同颜色空间的分量分布，RGB 适合查看颜色成分强度，HSI 更符合人眼对颜色的感知。
   * 直方图均衡化：RGB 空间均衡化可能出现假彩色现象，HSI 空间均衡化可提升亮度、对比度和色彩饱和度。
   * 均值滤波与拉普拉斯变换：在 RGB 和 HSI 空间分别进行操作，RGB 图像处理后边缘效果较好，HSI 图像仅保留少量细节。
6. **傅里叶变换与低通滤波**
   * 傅里叶变换：将图像转换到频率域，幅度谱图中心亮表示低频成分集中。
   * 低通滤波：包括理想、巴特沃斯和高斯低通滤波器，理想低通滤波器抑制高频导致振铃效应，巴特沃斯低通滤波器平滑性好，高斯低通滤波器过渡平滑，对边缘细节损失小。
7. **频率域和空间域拉普拉斯算子**
   * 空间域拉普拉斯算子：增强图像边缘，但易受噪声影响。
   * 频率域拉普拉斯算子：产生更平滑边缘效果，对噪声影响小，能增强边缘细节。

### （二）图像复原

1. **噪声添加**
   * 高斯、均匀、椒盐噪声：通过特定函数生成不同类型噪声，高斯噪声使灰度值分布扩展，均匀噪声类似，椒盐噪声在 0 和 255 处出现峰值。
2. **噪声滤波**
   * 算数平均、几何均值、最大值和最小值滤波器：分别对不同噪声有不同处理效果，如算数平均滤波器减少高斯噪声但模糊细节，几何均值滤波器抑制均匀噪声且保留一定边缘和细节，最大值滤波器去除椒盐噪声中的 “盐” 噪声但使图像轻微模糊。
3. **运动模糊与复原**
   * 运动模糊建模：通过点扩散函数模拟相机与物体相对运动造成的模糊。
   * 维纳滤波和最小乘方滤波：用于复原模糊加噪声图像，最小乘方滤波在清晰度上比维纳滤波效果更佳。

### （三）图像分割

1. **边缘检测**
   * Prewitt 梯度算子：包括水平和垂直方向算子，可检测图像边缘，水平算子突出垂直结构变化，对角线算子突出对角线方向特征。
   * Canny 算子：通过高斯滤波、梯度计算、非极大值抑制和双阈值处理检测边缘，产生的边缘细腻清晰，优于 Prewitt 算子。
2. **阈值分割**
   * Otsu 方法：基于最大化类间方差自动选取阈值分割图像，结合边缘检测可突出图像细节，减少背景细节。

### （四）计算机视觉

1. **主成分分析（PCA）**
   * 通过特征值分解对数据降维，在图像处理中实现图像压缩和重建，会损失少量信息。
   * 重构图像保留主要结构和轮廓，但细节模糊，如喷泉水流和建筑纹理细节丢失。
2. **方向梯度直方图（HOG）**
   * 计算图像局部梯度幅值和方向分布，构造特征向量。
   * 归一化后的直方图呈现一定特征，部分方向梯度特征强度较高。
3. **Harris 角点检测**
   * 根据窗口移动前后灰度变化检测角点。
   * 角点主要集中在建筑物窗格、文字和喷泉中心等区域。
4. **霍夫变换**
   * 将像素坐标转换到参数坐标，用于直线和圆形检测。
   * 在图像中成功检测到建筑物窗格和栏杆等直线。
5. **Viola Jones 人脸检测**
   * 利用 Haar-like 特征、积分图像、Adaboost 算法和级联结构实现人脸检测。
   * 在图片中识别出 16 张人脸，但有误识别一处非人脸区域的情况。

## 三、使用方法

### 安装依赖

确保已安装以下依赖库：

<pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>复制代码</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">pip install opencv-python numpy matplotlib scipy
</code></div></div></pre>

### 运行代码

根据需要运行相应的功能模块代码文件，传入图像路径和其他参数。例如，运行图像增强部分的灰度级切片处理：

<pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary select-none">python</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center select-none py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>复制代码</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-python">python grayscale_thresholding.py --image_path 'path_to_image.jpg' --threshold 128
</code></div></div></pre>

### 查看结果

处理后的图像会保存至指定目录或直接显示在窗口中。可以通过分析结果，进行调优或对比不同算法的效果。

## 四、贡献指南

欢迎对本项目进行改进和扩展。如果您有新的算法实现、功能优化或发现问题，请提交 Pull Request 或在 Issues 中讨论。

## 五、联系方式


如有疑问或建议，欢迎通过以下方式联系我：

* 电子邮件：[2891275548@qq.com]()

希望本项目能为数字图像处理的学习和研究提供有价值的参考和实践示例。

## 六、许可证

本项目采用 MIT 许可证，详细信息请查看 [LICENSE]() 文件。
