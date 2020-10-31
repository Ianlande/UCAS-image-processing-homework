#-*- coding:utf-8 -*-

"""
    二维快速傅里叶变换
    fft : 一维傅里叶变换
"""

import cv2 as cv
from numpy.fft import *
import numpy as np
import matplotlib.pyplot as plt


# 傅里叶变换
def dft2D(data):
    return fft(fft(data).T).T


# 谱图中心化
def dftshift(img):
    M,N = img.shape
    M = int(M/2)
    N = int(N/2)
    return np.vstack((np.hstack((img[M:,N:],img[M:,:N])),np.hstack((img[:M,N:],img[:M,:N]))))


# 对图片进行傅里叶变换测试
if __name__ == "__main__":
    img = r'images/lena_gray_512.tif'
    data = cv.imread(img, -1)
    output = dft2D(data)
    result = np.log(abs(dftshift(output))+1)
    
    # 输出
    plt.subplot(1,2,1)
    plt.title('origin_img')
    plt.imshow(data,cmap='gray')
    plt.subplot(1,2,2)
    plt.title('dft2d_img')
    plt.imshow(result,cmap='gray')
    plt.show()
    