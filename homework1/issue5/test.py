#-*- coding:utf-8 -*-

"""
    灰度图像高斯滤波
"""
import os
import sys
import cv2 as cv

# 设置导入地址
this_dir = os.path.dirname(os.path.abspath(__file__)) # 获得此程序地址
this_dir = os.path.dirname(this_dir) # 获取项目地址
sys.path.append(this_dir)

from issue3.twodConv import twodConv
from issue4.gaussKernel import gaussKernel


def main():
    img_ad = [r'../issue1/images/cameraman.tif',
              r'../issue1/images/einstein.tif',
              r'../issue2/output/lena512color_ntsc.jpg',
              r'../issue2/output/mandril_color_ntsc.jpg']
    
    # 没有文件夹则创建文件夹
    if os.path.exists(r"output") == False:
        os.mkdir(r"output")
    
    # 各卷积核
    for each_k in [1,2,3,5]:
        # 使用最常用的 3*3 和 5*5 卷积核进行测试
        for k_size in [3,5]:
            kernel = gaussKernel(each_k, k_size)
            # 各图像
            for each_img in img_ad:
                img = cv.imread(each_img, -1)
                # 两种边界填充方式
                for each in ['zero', 'replicate']:
                    output = twodConv(img, kernel, each)
                    
                    filename = each_img.split(r"/")[-1].split(r".")[0]
                    file = "output/"+filename+'_k'+str(each_k)+'_ks'+str(k_size)+'_'+str(each)+'.jpg'
                    print('dealing:  ', file)
                    cv.imwrite(file, output)


if __name__ == "__main__":
    main()
