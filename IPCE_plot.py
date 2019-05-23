#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# Author: Nick

import matplotlib.pyplot as plt
import os

folder = '' # folder为数据存放的文件夹

def get_files_list():  # get_files_list()是用来获取指定文件夹内所有文件的函数
    files_list = os.listdir(folder)  # 遍历指定文件夹内的所有文件，并存储到files_list列表中
    for i in files_list:
        if i[-4:] != ".txt":
            files_list.remove(i)
    print("共找到{}个文件：".format(len(files_list)))
    return files_list


def read_data(file_name):  # read_data函数用于读取文件内的数据
    print("现在处理文件：{}".format(file_name))
    file = open(folder + "\\" + file_name, 'r')
    data = file.readlines()  # data以行的形式读取IPCE文件中的数据
    file.close()
    x, y = [], []
    for i in data:
        if i[0:5] >= "200" and i[0:5] <= "900":  # 判断是否是数据行
            x.append(float(i.split('\t')[0]))  # 以\t分割每一行的数据，第1列为波长WD
            y.append(float(i.split('\t')[1]))  # 第2列为纵坐标IPCE
        if i[0:12] == "Jsc [mA/cm2]":
            jsc = float(i[15:20])
    return x, y, jsc

def integrate(x, y):
    ans = [0]
    for i in range(1, len(x)):
        ans.append(ans[i-1] + (y[i]+y[i-1])*(x[i]-x[i-1])/2)
    return ans

def plot(x, y1, jsc, file):  # plot为用以画图的函数
    fig = plt.figure()  # 创建一个对象fig
    ax1 = fig.add_subplot(111)  # 创建一个1行*1列的画布，将子图画在从左至右的第1块
    ax1.plot(x, y1) # 首先绘制IPCE曲线
    ax1.set_ylabel("IPCE (%)")
    ax1.set_xlabel("Wavelength (nm)")
    ax1.set_xlim(300, 850)
    ax1.set_ylim(0, 90)
    ax1.set_title("{}    $Jsc$={} mA/$\\rm cm^2$".format(file, str(jsc)))  # 为图片添加标题（$$内为latex格式的公式）

    # 接下来绘制积分电流曲线
    integrate_y = integrate(x, y1)  #算出积分后的y值
    y2 = []
    for i in integrate_y:
        y2.append(i/integrate_y[-1]*jsc)  #将y值标准化，使得最后一个值等于jsc
    ax2 = ax1.twinx()  # 创建双y轴图
    ax2.plot(x, y2, 'r')
    ax2.set_ylabel("Integrate Current (mA/$\\rm cm^2$)")
    ax2.set_ylim(0, 25)
    plt.savefig(folder + "\\" + file[:-4] + ".png", dpi = 600)
    plt.show()

#主程序开始
if __name__ == '__main__':
    print("欢迎使用IPCE自动画图器---版本：1.2---Coder：Nick")
    folder = input(r"请输入存放IPCE数据的文件夹（所有生成的图像文件将自动保存到该文件夹）：")
    ipce_list = get_files_list()
    for i in ipce_list:
        x, y, jsc = read_data(i)
        plot(x, y, jsc, i)