#-*- coding:utf-8 -*-

"""
    测试图像二维快速傅里叶变换与逆变换
"""

import os
import sys
import cv2 as cv
from numpy.fft import *
import numpy as np
import matplotlib.pyplot as plt

# 设置导入地址
this_dir = os.path.dirname(os.path.abspath(__file__)) # 获得此程序地址
this_dir = os.path.dirname(this_dir) # 获取项目地址
sys.path.append(this_dir)

from issue1.dft2d import dft2D, dftshift
from issue2.idft2d import idft2D


# 归一化
def normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range


# 对图片进行测试: 傅里叶变换; 傅里叶反变换
def main():
    img = r'images/rose512.tif'
    origin_img = cv.imread(img, -1) # 原图
    origin_img = normalization(origin_img)
    temp = dft2D(origin_img)
    dft2D_img = np.log(abs(dftshift(temp))+1) # 傅里叶变换
    temp = idft2D(temp)
    idft2D_img = np.abs(temp) # 逆傅里叶变换
    error_img = origin_img-idft2D_img # 误差图像
    
    print('原图像 与 正负傅里叶变换后重新生成图像 的误差 : ',np.linalg.norm(origin_img-idft2D_img))
    
    # 输出
    plt.subplot(2,2,1)
    plt.title('origin_img')
    plt.imshow(origin_img,cmap='gray')
    plt.subplot(2,2,2)
    plt.title('dft2d_img')
    plt.imshow(dft2D_img,cmap='gray')
    plt.subplot(2,2,3)
    plt.title('idft2d_img')
    plt.imshow(idft2D_img,cmap='gray')
    plt.subplot(2,2,4)
    plt.title('error_img')
    plt.imshow(error_img,cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()