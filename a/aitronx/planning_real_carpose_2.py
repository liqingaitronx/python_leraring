import numpy as np
import matplotlib.pyplot as plt
# import easygui
import sys
import os
from collections import Counter



def parse_real_path(filename):
    # 存储 x 和 y 的数据点
    x_data = []
    y_data = []
    with open(filename, 'r',encoding='utf-8') as f:
        for line in f:
            # 查找 "cur.x: " 字符串在当前行的位置
            pos = line.find("cur.x: ")
            # 如果字符串不在当前行中，则跳过当前行
            if -1 == pos:
                continue
            # 从当前行的字符串中提取 x 的值
            line = line[pos+7:]
            # 查找 ", y:" 字符串在当前行的位置
            pos = line.find(", y:")
            # 如果字符串不在当前行中，则跳过当前行
            if -1 == pos:
               # print("bad input line: {}".format(line))
                continue
            # 将提取的 x 值添加到 x_data 中
            x_data.append(float(int(line[:pos])/1000))
            # 从当前行的字符串中提取 y 的值
            line = line[pos+4:]
            # 查找 ", theta" 字符串在当前行的位置
            pos = line.find(", theta")
            # 如果字符串不在当前行中，则跳过当前行
            if -1 == pos:
              #  print("bad input line: {}".format(line))
                continue
            # 将提取的 y 值添加到 y_data 中
            y_data.append(float(int(line[:pos])/1000))

    # 将列表转换为 NumPy 数组并返回
    return np.asarray(x_data), np.asarray(y_data)


def parse_planing_path(filename):
    x_data = []
    y_data = []
    with open(filename, 'r',encoding='utf-8') as f:
        for line in f:
            pos = line.find("way.x: ")
            if -1 == pos:
                continue
            line = line[pos+7:]
            pos = line.find(", y:")
            if -1 == pos:
                print("bad input line: {}".format(line))
                continue
            x_data.append(float(int(line[:pos])/1000))
            line = line[pos+4:]

            pos = line.find(", theta")
            if -1 == pos:
                print("bad input line: {}".format(line))
                continue
            y_data.append(float(int(line[:pos])/1000))

    return np.asarray(x_data), np.asarray(y_data)

def GetXYAngLast(testlist):
    x_Lastlist,y_Lastlist= \
    [[] for i in range(2)]
    with open(testlist, 'r', encoding='utf-8') as f:
        for line in f:
            # print(line)
            if "GetXYAngLast" in line:
                # line[line.index("t x:") + 4:line.index(",") + 0]
                x_Lastlist.append(float(line[line.index("t x:") + 4:line.index(",") + 0]))
                y_Lastlist.append(float(line[line.index(",y:") + 3:line.index(",ang") + 0]))
        return x_Lastlist,y_Lastlist#算法路径

def main():
    x_real, y_real = parse_real_path("patherro-1（斜向）.log")
    x_plan, y_plan = parse_planing_path("patherro-1（斜向）.log")
    x_Lastlist, y_Lastlist = GetXYAngLast("xiexiang.txt")

    # print("wheelspeed shape: ", wheelspeed.shape)
    plt.plot(x_real, y_real, 'c', label="real path")
    plt.plot(x_plan, y_plan, 'r.-', label="planing path")
    plt.plot(x_Lastlist, y_Lastlist, 'y', label="GetXYAngLast")

    output_dir = '/Users/lizitao/Desktop/'
    # 如果不存在，则创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    if not os.path.exists(os.path.join(output_dir, 'slart_coord')):
        os.makedirs(os.path.join(output_dir, 'slart_coord'))
    #将realpath写入到指定目录
    output_file = os.path.join(output_dir, 'slart_coord', 'real_path.txt')
    with open(output_file, 'w') as f:
        f.write('real_path.txtX,real_path.txtY\n')
        for i in range(len(x_real)):
            f.write(str(x_real[i]) + ',' + str(y_real[i]) + '\n')

    # 将x_plan和y_plan写入文件planning_path.txt中
    output_file = os.path.join(output_dir, 'slart_coord', 'planning_path.txt')
    with open(output_file, 'w') as f:
        f.write('planning_pathX,planning_pathY\n')
        for i in range(len(y_plan)):
            f.write(str(x_plan[i]) + ',' + str(y_plan[i]) + '\n')

        print(i)

    # 将x_Lastlist和y_Lastlist写入文件last_list.txt中
    output_file = os.path.join(output_dir, 'slart_coord', 'GetXYAngLast.txt')
    with open(output_file, 'w') as f:
        f.write('GetXYAngLastX,GetXYAngLastY\n')
        for i in range(len(x_Lastlist)):
            f.write(str(x_Lastlist[i]) + ',' + str(y_Lastlist[i]) + '\n')


    #写入当前目录-----
    # with open('real_path.txt', 'w') as f:
    #     f.write('X,Y\n')
    #     for i in range(len(x_real)):
    #         f.write(str(x_real[i]) + ',' + str(y_real[i]) + '\n')

    plt.legend()
    # plt.xlim(0, 5)
    # plt.ylim(-10, 10)
    plt.xlabel("x(m)")
    plt.ylabel('y(m)')
    plt.title("planing real path compare")
    plt.show()


if __name__ == "__main__":
    main()