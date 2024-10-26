# 数字图像处理测试

欢迎来到数字图像处理测试仓库！该项目旨在提供一系列用 Python 实现的图像处理技术和测试，作为理解和实验各种图像处理算法的实用指南。

## 目录

* [功能](#%E5%8A%9F%E8%83%BD)
* [安装](#%E5%AE%89%E8%A3%85)
* [使用方法](#%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95)
* [图像处理技术](#%E5%9B%BE%E5%83%8F%E5%A4%84%E7%90%86%E6%8A%80%E6%9C%AF)
* [贡献](#%E8%B4%A1%E7%8C%AE)
* [许可证](#%E8%AE%B8%E5%8F%AF%E8%AF%81)

## 功能

* 基本图像操作（调整大小、裁剪、旋转）
* 图像滤波（模糊、锐化、边缘检测）
* 颜色空间转换（RGB 转灰度、HSV 等）
* 噪声减少技术
* 图像增强算法

## 安装

要开始使用此项目，请克隆仓库并安装所需的依赖项：

<pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>复制代码</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">git clone https://github.com/Enqd/Digital-image-processing-test.git
cd Digital-image-processing-test
pip install -r requirements.txt
</code></div></div></pre>

## 使用方法

您可以运行 `src` 目录中的脚本来测试各种图像处理技术。例如：

<pre class="!overflow-visible"><div class="contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative bg-token-sidebar-surface-primary dark:bg-gray-950"><div class="flex items-center text-token-text-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9 bg-token-sidebar-surface-primary dark:bg-token-main-surface-secondary">bash</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-sidebar-surface-primary px-2 font-sans text-xs text-token-text-secondary dark:bg-token-main-surface-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg>复制代码</button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-bash">python src/example_script.py
</code></div></div></pre>

请确保将 `example_script.py` 替换为所需的脚本名称。

## 图像处理技术

这里可以列出实现的具体技术，例如：

* 图像模糊
* 边缘检测
* 直方图均衡
* 彩色图像处理
* 噪声去除

## 贡献

欢迎贡献代码或提出建议！请先阅读 [贡献指南](CONTRIBUTING.md)，了解如何参与。

## 许可证

该项目采用 MIT 许可证，详细信息请查看 [LICENSE]() 文件。
