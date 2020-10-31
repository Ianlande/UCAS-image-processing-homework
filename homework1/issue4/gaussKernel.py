#-*- coding:utf-8 -*-

"""
    归一化二维高斯滤波核函数
"""

import math
import numpy as np

"""
input:
    sig : 高斯函数中的 sigmoid
    m : 核尺寸 m*m
output:
    高斯滤波核, array 类型, dtype=np.float32
"""
def gaussKernel(sig, m=-1):
    # 如果不设置参数
    if m == -1:
        m = math.ceil(3*sig) * 2 + 1
        
    # 如果 m 过小
    if m < 2:
        print("Warning: 设定的卷积核过小")
        
    # 初始化 output
    output = np.zeros((m,m),dtype=np.float32)
    
    # 计算
    for eachline in range(m):
        for eachcol in range(m):
            x = eachline - (m-1)/2
            y = eachcol - (m-1)/2
            temp = math.exp(-(x*x + y*y)/(2*sig*sig))
            output[eachline][eachcol] = temp / (2*math.pi*sig*sig)
            
    # 归一化
    output = output / np.sum(output)
    
    return output


def main():
    print(gaussKernel(1,3))


if __name__ == "__main__":
    main()
