#-*- coding:utf-8 -*-

"""
    与 python 自带的函数库存进行比较
"""

import cv2 as cv
import numpy as np
import scipy.signal as signal


# 使用 opencv 自带的函数实现二维高斯卷积核
# 取 sigma = 1, kernel_size = 3
def gaussian_kernel_2d_opencv(kernel_size = 3,sigma = 1):
    kx = cv.getGaussianKernel(kernel_size,sigma)
    ky = cv.getGaussianKernel(kernel_size,sigma)
    return np.multiply(kx,np.transpose(ky)) 


def main():
    # 项目生成的图片
    img_ad = r'output/cameraman_k1_ks3_replicate.jpg'
    img = cv.imread(img_ad, -1)
    
    # 原图片
    img_c_ad = r'../issue1/images/cameraman.tif'
    img_c = cv.imread(img_c_ad, -1)
    
    # 用 python 自带函数实现
    kernel = gaussian_kernel_2d_opencv()
    img_new = signal.convolve2d(img_c,kernel,boundary='symm',mode='same')
    
    # 计算两种方式的误差
    img = np.array(img,dtype='int')
    img_new = np.array(img_new,dtype='int')
    error = abs(img_new - img)
    
    # 差值矩阵
    print("error:")
    print(error)
    
    # 差值图像
    cv.imshow("error", np.array(error,dtype='uint8'))
    cv.waitKey(0)


if __name__ == "__main__":
    main()
