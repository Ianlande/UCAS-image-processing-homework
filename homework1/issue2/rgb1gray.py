#-*- coding:utf-8 -*-

"""
    彩色图像转换为黑白图像
"""

import os
import cv2 as cv
import matplotlib.pyplot as plt


"""
input : 
    img : 图像
    method : 参数 , ntsc 或者 NTSC 表示用 NTSC 方法; average 表示用 average 方法
output : 
    
"""
def rgb1gray(img, method="ntsc"):
    img = cv.imread(img)
    
    img_r = img[:, :, 0]
    img_g = img[:, :, 1]
    img_b = img[:, :, 2]
    
    if method == 'average':
        # 不能 (img_r+img_g+img_b)/3, (img_r+img_g+img_b) 会直接大于 255 溢出
        output = img_r / 3 + img_g / 3 + img_b / 3
        return output
    elif method == 'ntsc':
        output = img_r * 0.2989 + img_g * 0.5870 + img_b * 0.1140
        return output
    else:
        print("参数错误, method 只能是 average 或者 ntsc")


def main():
    img_ad = [r'images/lena512color.tiff', r'images/mandril_color.tif']
    
    for eachImg in img_ad:
    
        # 没有文件夹则创建文件夹
        if os.path.exists(r"output") == False:
            os.mkdir(r"output")
        
        output_average = rgb1gray(eachImg, "average")
        output_ntsc = rgb1gray(eachImg, "ntsc")
        
        filename = "output/" + eachImg.split(r"/")[1].split(r".")[0] + '_average.jpg'
        cv.imwrite(filename, output_average)
        filename = "output/" + eachImg.split(r"/")[1].split(r".")[0] + '_ntsc.jpg'
        cv.imwrite(filename, output_ntsc)


if __name__ == "__main__":
    main()