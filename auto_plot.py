#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: Nick
import JV_plot, IPCE_plot  # JV_plot和IPCE_plot分别为绘制JV曲线和IPCE曲线的子程序
import tkinter as tk
from tkinter import filedialog # filedialog用于弹出选择文件的对话框

iv_files = ()  # iv_files为jv数据文件的名称（以list形式存放）
ipce_files = []  # ipce_files为ipce数据文件的名称（以list形式存放）

def jv_search_file():
    global iv_files, ipce_files
    if choose.get() == 1:
        iv_files = filedialog.askopenfilenames(filetypes=[("TXT",".txt"),("全部文件",".*")])
        jv_import()
    elif choose.get() == 2:
        ipce_files = filedialog.askopenfilenames(filetypes=[("TXT",".txt"),("全部文件",".*")])
        ipce_import()
    return None
def jv_import():
    # jv_import函数用于读取指定路径内的数据文件，并将其添加到jv_label中
    global iv_files  # iv_files声明为全局变量
    var.set('共找到{}个文件：'.format(len(iv_files)))  # var为jv_label中显示的内容
    for i in iv_files:
        var.set(var.get() + '\n' + i)  # 将找到的文件添加到显示框中
    var.set(var.get() + '\n\n' + '导入数据文件成功！请点击“开始画图”按钮画图')
    return None

def ipce_import():
    # ipce_import函数用于读取指定路径内的数据文件，并将其添加到jv_label中
    global ipce_files  # ipce_files声明为全局变量
    var.set('共找到{}个文件：'.format(len(ipce_files)))
    for i in ipce_files:
        var.set(var.get() + '\n' + i)  # 将找到的文件添加到显示框中
    var.set(var.get() + '\n\n' + '导入数据文件成功！请点击“开始画图”按钮画图')
    return None

def jv_plot():
    # 对jv曲线画图的函数
    global iv_files
    for i in iv_files:
        JV_plot.plot(i)
    var.set(var.get() + '\n' + '画图成功！请到数据文件夹内查看！')
    return None

def ipce_plot():
    # 对ipce曲线画图的函数
    global ipce_files
    for i in ipce_files:
        x, y, jsc = IPCE_plot.read_data(i)
        IPCE_plot.plot(x, y, jsc, i)
    return None

if __name__ == '__main__':
    root = tk.Tk()  # 实例化root
    root.title('实验室数据自动画图器(Lin Group)')  # 设置窗口标题
    root.geometry('500x400')  # 设置窗口大小

    # 设置最上方的欢迎文字
    hello_label = tk.Label(root, text='欢迎使用自动画图器！----Coder：Nick',
                           height=2, justify='center')  # height设置高度，justify设置对齐方式为居中
    hello_label.grid(row=0, column=0, columnspan=2, sticky=tk.W+tk.E)  # 将其设置在0行0列，占据2列

    # 设置JV_Plot的Frame：jv_frame
    jv_frame = tk.Frame(root, bd=2, relief='groove',  # 设置边框bd=1, 边框样式groove
                        padx=5,pady=5)   # 设置框架内其他组件离边框的水平和垂直距离
    jv_frame.grid(row=1,column=0)  # jv_frame放在1行0列

    # 设置两个单选按钮以选择JV还是IPCE
    choose = tk.IntVar()  # choose用于判断单选按钮选择了谁
    choose.set(1)  # 默认选择1，即jv画图
    select1 = tk.Radiobutton(jv_frame, text='JV曲线画图', variable=choose, value=1)  # 单选按钮1，jv画图
    select1.grid(row=1,column=0)
    select2 = tk.Radiobutton(jv_frame, text='IPCE曲线画图', variable=choose, value=2) # 单选按钮2，ipce画图
    select2.grid(row=1,column=1)

    # 设置一个文本框（jv_label）用于显示目前jv_plot的状态
    var = tk.StringVar()  # 新建一个文字变量储存器用于更改jv_label的内容
    jv_label = tk.Label(jv_frame, textvariable=var, width=60,  # 使用 textvariable 替换 text, 因为这个是可以变化的
                        height=15, bg='AliceBlue',    # 高度15，背景颜色：灰色
                        justify='left',anchor='nw')  #justify：左对齐；anchor：文字位于控件的左上角
    jv_label.grid(row=3, column=0, columnspan=2, sticky=tk.W+tk.E)

    # 设置浏览文件的按钮
    jv_file = tk.Button(jv_frame, text="浏览", height=2, width=20,
                        command=jv_search_file)
    jv_file.grid(row=4, column=0, sticky=tk.W + tk.E, padx=0)  # sticky=tk.W+tk.E意思是向左和向右对齐，即水平方向拉伸到边界

    # 设置一个开始画图的按钮
    jv_plot_button = tk.Button(jv_frame, text='开始画图', height=2, width=20,
                               command = lambda :jv_plot() if choose.get()==1 else ipce_plot())  # 点击按钮执行的命令
    jv_plot_button.grid(row=4,column=1, sticky=tk.E)

    root.mainloop()  # 显示窗口
