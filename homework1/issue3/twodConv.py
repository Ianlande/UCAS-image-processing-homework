#-*- coding:utf-8 -*-

"""
    图像二维卷积函数
"""

import numpy as np

"""
input:
    img : 图像, array 类型, dtype=uint8
    w : 核函数, array 类型, dtype=float32
        目前只支持行列数相同的核, 例如 m*m ,不支持 m*n 的核
    arg : 边界填充参数 replicate or zero
output:
    图像, array 类型
"""
def twodConv(img, w, arg='zero'):
    img_height, img_width = img.shape
    w_height, w_width = w.shape
    
    # 初始化 output
    output = np.zeros((img_height,img_width),dtype=np.uint8)
    
    # 目前只支持卷积核行列数相同
    if w_height != w_width:
        print("卷积核行列数应相同")
        return -1
        
    # 填充数
    pad_num = int((w_height - 1) / 2)
    
    # padding
    for each in range(pad_num):
        if arg == 'zero':
            img_height, img_width = img.shape
            temp = np.zeros((1,img_height),dtype=np.uint8)
            img = np.insert(img, 0, temp, axis=1)
            img = np.insert(img, img_width+1, temp, axis=1)
            
            img_height, img_width = img.shape
            temp = np.zeros((1,img_width),dtype=np.uint8)
            img = np.insert(img, 0, temp, axis=0)
            img = np.insert(img, img_height+1, temp, axis=0)
            #print(img)
        elif arg == 'replicate':
            img_height, img_width = img.shape
            temp = img[:,0]
            img = np.insert(img, 0, temp, axis=1)
            temp = img[:,-1]
            img = np.insert(img, img_width+1, temp, axis=1)
            
            img_height, img_width = img.shape
            temp = img[0,:]
            img = np.insert(img, 0, temp, axis=0)
            temp = img[-1,:]
            img = np.insert(img, img_height+1, temp, axis=0)
            #print(img)
        else:
            print("参数错误, arg 只能是 zero 或者 replicate")
            
    # 卷积
    output_h, output_w = output.shape
    for eachline in range(output_h):
        for eachcol in range(output_w):
            extract = img[eachline:eachline+w_height, eachcol:eachcol+w_width]
            output[eachline][eachcol] = int(np.sum(extract * w))
    
    return output


def main():
    img = np.array([[7,6,5,5,6,7],
                    [6,4,3,3,4,6],
                    [5,3,2,2,3,5],
                    [5,3,2,2,3,5],
                    [6,4,3,3,4,6],
                    [7,6,5,5,6,7]])
    w = np.array([[ 0.,-1., 0.],
                  [-1., 5.,-1.],
                  [ 0.,-1., 0.]])
    output = twodConv(img, w, 'replicate')
    print("output:")
    print(output)


if __name__ == "__main__":
    main()
