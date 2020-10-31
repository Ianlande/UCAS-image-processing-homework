# 2020年秋季学期 图像处理与分析 编程作业01

## 整体说明：
第一至第五题分别在 issue1 至 issue5, 程序已经写好注释, 注释见程序中, 输出结果见各个 output 文件夹


## homework1 文件说明:
issue1 : 题目一  
issue2 : 题目二  
issue3 : 题目三  
issue4 : 题目四  
issue5 : 题目五  


## 详细说明：

### 第一题：黑白图像灰度扫描
scanLine4e.py : 程序, 将 images 文件夹中的图片按题目要求进行处理, 储存至 output 文件夹中  
images : 储存被处理的图片  
output :   
        输出的结果 : cameraman.tif 的中心行和中心列图, einstein.tif 的中心行和中心列图, 一共四张  
        可以在程序中修改输出 折线图 或者 柱状图  

### 第二题：彩色图像转换为黑白图像  
rgb1gray.py : 程序, 将 images 文件夹中的图片按题目要求进行处理, 储存至 output 文件夹中  
images : 储存被处理的图片  
output :   
        输出的结果 : mandril_color.tif, lena512color.tiff 分别使用 average 和 NTSC 方式进行处理  
对两种方法的结果进行比较:  
    average 方式处理得到的图片比 NTSC 方式更加淡  

### 第三题：图像二维卷积函数
twodConv.py : 程序

### 第四题：归一化二维高斯滤波核函数
gaussKernel.py : 程序

### 第五题：灰度图像的高斯滤波
output : 输出的结果  
test.py :  
         调用第三题的 twodConv 和第四题的 gaussKernel 函数, 对第一第二题的图片进行处理  
         遍历四张图片; sigma = 1,2,3,5 ; 每张图片分别使用 `3*3,5*5` 卷积核, 分别使用 zero 和 replicate 卷积边界填充方式  
         因此一共输出 `4*4*2*2 = 64` 张图片  
         每张图片的命名规则: `图片名_k(sigma大小)_ks(卷积核尺寸)_(卷积边界填充方式).jpg`  
         结果均在 output 文件夹中  
compare.py :   
         用 python 自带的库, 实现 图像二维卷积函数 和 归一化二维高斯滤波核函数, 进行灰度图像的高斯滤波  
         在 sigma=1, 核尺寸=3*3 条件下, 对 cameraman.tif 进行测试  
         两者对比后, 计算差值矩阵 error, 并输出差值图像  
         
比较其他参数条件不变的情况下像素复制和补零下滤波结果在边界上的差别:  
对 output 中的 64 张图片进行比较, 发现使用补零方式处理, 图片会有一条黑边  
