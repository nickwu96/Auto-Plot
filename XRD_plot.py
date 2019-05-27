#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: Nick
import matplotlib.pyplot as plt
import os

folder = '' # 定义全局变量folder

def get_files_list():  # get_files_list()是用来获取指定文件夹内所有文件的函数
    files_list = os.listdir(folder)  # 遍历指定文件夹内的所有文件，并存储到files_list列表中
    xrd_list = []
    for i in files_list:
        if i[-4:] == ".txt":
            xrd_list.append(i)
    print("共找到{}个文件：".format(len(xrd_list)))
    return xrd_list

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

def plot(file_name):  # plot为用以画图的函数
    # 开始画图
    #plt.xlim(0, 1.2)
    #plt.ylim(0, 25)
    plt.title(file_name)
    plt.plot(x, y)
    plt.scatter(x, y, s=8)
    plt.xlabel('Voltage(V)')
    plt.ylabel('Current Density(mA/cm2)')
    plt.savefig(folder + "\\" + file_name[:-4] + ".png", dpi=600)
    plt.show()

if __name__ == '__main__':
    print("欢迎使用自动画图器---版本：1.1---Coder：Nick")
    # folder = input(r"请输入存放数据的文件夹（所有生成的图像文件将自动保存到该文件夹）：")
    folder = r"D:\科研\博士科研\实验数据\2019.5.7-XRD"
    xrd_files = get_files_list()
    for i in xrd_files:
        print(i)
    print("接下来分别对每个文件的数据画图：")
    for i in xrd_files:
        plot(i)