#-*- coding:utf-8 -*-

"""
    计算图像的中心化二维快速傅里叶变换与谱图像
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
from issue3.normalization import normalization


# 生成图像
def create_img(img_w, img_h, iw, ih, path):
    data = np.zeros((img_h, img_w),dtype=np.uint8)
    index_h = img_h/2 - ih/2
    index_w = img_w/2 - iw/2
    data[int(index_h):int(index_h+ih+1),int(index_w):int(index_w+iw+1)] = 255
    cv.imwrite(path, data)


def main():
    img_path = r"images/img.jpg" # 图像路径
    
    # 没有文件夹则创建文件夹
    if os.path.exists(r"images") == False:
        os.mkdir(r"images")
    
    create_img(512,512,10,60,img_path) # 生成图像
    
    origin_img = cv.imread(img_path, -1)
    nor_img = normalization(origin_img) # 原图
    dft_img = dft2D(nor_img) # 谱图像
    dft_shift_img = dftshift(dft_img) # 中心化谱图
    output_img = np.log(abs(dft_shift_img)+1) # 对数变换后谱图
    
    # 输出
    plt.subplot(2,2,1)
    plt.title('origin_img')
    plt.imshow(origin_img,cmap='gray')
    plt.subplot(2,2,2)
    plt.title('dft_img')
    plt.imshow(abs(dft_img),cmap='gray')
    plt.subplot(2,2,3)
    plt.title('dft_shift_img')
    plt.imshow(abs(dft_shift_img),cmap='gray')
    plt.subplot(2,2,4)
    plt.title('output_img')
    plt.imshow(output_img,cmap='gray')
    plt.show()


if __name__ == "__main__":
    main()