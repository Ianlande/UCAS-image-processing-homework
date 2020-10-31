#-*- coding:utf-8 -*-

"""
    二维逆傅里叶变换
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


# 傅里叶反变换
def idft2D(data):
    M,N = data.shape
    return (fft(fft(data.conjugate()).T).T / (M*N)).conjugate()


# 对图片进行测试: 傅里叶变换; 傅里叶反变换
if __name__ == "__main__":
    img = r'images/lena_gray_512.tif'
    origin_img = cv.imread(img, -1) # 原图
    temp = dft2D(origin_img)
    dft2D_img = np.log(abs(dftshift(temp))+1) # 傅里叶变换
    temp = idft2D(temp)
    idft2D_img = np.abs(temp) # 逆傅里叶变换
    
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
    plt.show()
    