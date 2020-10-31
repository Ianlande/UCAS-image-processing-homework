#-*- coding:utf-8 -*-

"""
    附加题
"""

import os
import sys
import math
import cv2 as cv
from numpy.fft import *
import numpy as np
import matplotlib.pyplot as plt

# 设置导入地址
this_dir = os.path.dirname(os.path.abspath(__file__)) # 获得此程序地址
this_dir_last = os.path.dirname(this_dir) # 获取项目地址
sys.path.append(this_dir_last)

from issue1.dft2d import dft2D, dftshift
from issue3.normalization import normalization


# 图片预处理: 解决尺寸不正确, 图片多通道等问题
def pre_dealing(data):
    # ========= 如果有多个通道 =========
    if len(data.shape) > 2:
        data = data[:,:,0]
    
    # ========= 如果尺寸不是2的整数次幂 =========
    size = []
    m, n = data.shape
    size.append(m)
    size.append(n)
    
    for index in range(len(size)):
        result = size[index] & (size[index]-1)
        if result != 0:
            neighbo_num = math.log(size[index],2)
            neighbo_num = math.ceil(neighbo_num)
            size[index] = int(math.pow(2, neighbo_num)) # 新尺寸
    
    size[0]-=m
    size[1]-=n
    m_h = int(size[0]/2)
    m_w = int(size[0]) - int(size[0]/2)
    n_h = int(size[1]/2)
    n_w = int(size[1]) - int(size[1]/2)
    
    data = np.pad(data,pad_width=((m_h,m_w),(n_h,n_w)),mode='constant',constant_values=(0))
    
    return data


def main():
    file_path = r"images"
    
    imgs_name = []
    imgs_path = []
    for root, dirs, files in os.walk(file_path):  
        for path in files:
            imgs_path.append(path)
            name = path.split('.')[0]
            imgs_name.append(name)
    
    for index in range(len(imgs_path)):
        img_path = file_path + '/' + imgs_path[index]
        
        img = cv.imread(img_path, -1)
        origin_img = pre_dealing(img)
        origin_img = normalization(origin_img) # 原图
        dft_img = dft2D(origin_img) # 谱图像
        dft_shift_img = dftshift(dft_img) # 中心化谱图
        output_img = np.log(abs(dft_shift_img)+1) # 对数变换后谱图
        
        plt.subplot(2,len(imgs_path),index+1)
        plt.title(imgs_name[index])
        plt.imshow(img,cmap='gray')
        plt.subplot(2,len(imgs_path),index+1+len(imgs_path))
        plt.title(imgs_name[index]+'_dft')
        plt.imshow(output_img,cmap='gray')
    
    plt.show()


if __name__ == "__main__":
    main()