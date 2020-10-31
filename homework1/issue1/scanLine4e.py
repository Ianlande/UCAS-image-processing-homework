#-*- coding:utf-8 -*-

"""
    黑白图像灰度扫描
"""

import os
import cv2 as cv
import matplotlib.pyplot as plt


"""
input: 
    img : 灰度单通道图像;
    i : 图像行数或者列数;
    arg : row 或者 column
output:
    图像第 i 行或列;
    type: list
"""
def scanLine4e(img, i, arg):
    img = cv.imread(img, -1)
    
    if arg == "row":
        output = list(img[int(i)])
        return output
    elif arg == "column":
        output = []
        for eachLine in img:
            output.append(eachLine[int(i)])
        return output
    else:
        print("参数错误, arg 只能是 row 或者 column")


"""
input : 
    arg : bar 或者 line , 分别表示返回 柱状图 或者 折线图 , 默认柱状图
output : 
    图片形式返回, 储存在 output 文件夹里面
    返回的图片命名规则 : 图片名称 + 行或列
"""
def main(arg='bar'):
    img_ad = [r'images/cameraman.tif', r'images/einstein.tif']
    
    for eachImg in img_ad:
        img = cv.imread(eachImg, -1) # -1 表示保留原通道数
        
        # 图像基本信息
        size = img.shape
        row = size[0]
        column = size[1]
        
        #print("size:    ",size)
        #print("row:    ",row)
        #print("column:    ",column)
        
        # 获取图像的中心行和中心列值
        output_row = scanLine4e(eachImg, row/2, 'row')
        output_column = scanLine4e(eachImg, column/2, 'column')
        
        # 没有文件夹则创建文件夹
        if os.path.exists(r"output") == False:
            os.mkdir(r"output")
            
        # 保存结果
        fig = plt.figure()
        if arg == 'bar':
            plt.bar(range(column), output_row , 0.4, color="green")
            plt.title("bar graph")
        elif arg == 'line':
            plt.plot(range(column), output_row)
            plt.title("line graph")
        else:
            print("参数错误, arg 只能是 bar 或者 line")
            
        plt.xlabel("index")
        plt.ylabel("figure")
        plt.savefig("output/" + str(eachImg.split(r"/")[-1][:-4] + '_row.jpg'))
        
        fig = plt.figure()
        if arg == 'bar':
            plt.bar(range(row), output_column , 0.4, color="green")
            plt.title("bar graph")
        elif arg == 'line':
            plt.plot(range(row), output_column)
            plt.title("line graph")
        else:
            print("参数错误, arg 只能是 bar 或者 line")
            
        plt.xlabel("index")
        plt.ylabel("figure")
        plt.savefig("output/" + str(eachImg.split("/")[-1][:-4]) + str("_column.jpg"))


if __name__ == "__main__":
    main(arg='bar')
