import matplotlib.pyplot as plt
import os

folder = ''   # folder为存放数据的文件夹

def get_files_list():  #get_files_list()是用来获取指定文件夹内所有文件的函数
    files_list = os.listdir(folder)  # 遍历指定文件夹内的所有文件，并存储到files_list列表中
    iv_files, files_nums = [], 0  # iv_files用于存储所有的iv文件，files_num记录总文件数
    for i in files_list:
        if i[-3:] == 'txt' and i[-7:-4] != '-iv':
            iv_files.append(i)
            files_nums += 1
    print("共找到{}个文件：".format(files_nums))
    return iv_files

def plot(file_name):
    measurement = ''
    result = []
    # 单个结果文件读取
    graph_file_name = file_name[:-4] + '-iv.txt'
    f = open(folder+'\\'+file_name, 'r')
    measurement = f.readlines()
    f.close()
    f = open(folder+'\\'+graph_file_name, 'r')
    graph = f.readlines()
    f.close()

    # 各条数据预处理，结果存在whole_result列表中
    for i in measurement:
        line = i.split('\t')  #每一行的数据内容，以list形式存储
        one_result = {'Voc': line[1], 'Jsc': line[3], 'FF': line[7], 'Efficiency': line[8]}  #每一个电池的结果
        result.append(one_result)  #所有电池的结果
    del result[0]  #删除表头信息

    best_efficiency = 0  #最佳效率
    best = 0  #最佳效率的位置（是第几条电池）

    for i in range(1,len(result)):
        if float(result[i]['Efficiency']) > best_efficiency and float(result[i]['Efficiency']) < 25:
            best_efficiency = float(result[i]['Efficiency'])
            best = i

    # 画图数据预处理
    x, y = [], []
    for i in range(2, len(graph)):
        line = graph[i].split('\t')  #每一行的数据内容，以list形式存储
        x.append(float(line[best*2]))
        y.append(float(line[best*2+1])*1000/0.06)
    print("文件{}：最高效率{}，来自第{}条电池".format(file_name, best_efficiency, best+1))

    #开始画图
    plt.xlim(0,1.2)
    plt.ylim(0,25)
    plt.title(file_name + '(PCE：' + str(best_efficiency) + ')',fontproperties='SimHei')
    plt.plot(x, y)
    plt.scatter(x, y, s=8)
    plt.xlabel('Voltage(V)')
    plt.ylabel('Current Density(mA/cm2)')
    plt.savefig(folder+"\\"+file_name[:-4]+".png", dpi=600)
    plt.show()

#主程序开始
if __name__ == '__main__':
    print("欢迎使用自动画图器---版本：1.1---Coder：Nick")
    # folder = input(r"请输入存放数据的文件夹（所有生成的图像文件将自动保存到该文件夹）：")
    folder = r"D:\科研\博士科研\实验数据\2019.4.30-JV"
    iv_files = get_files_list()
    for i in iv_files:
        print(i)
    print("接下来分别对每个文件的数据画图：")
    for i in iv_files:
        plot(i)

#打包成exe：pyinstaller -F D:\学习\Python\Pycharm\JV_plot.py