import numpy as np
import matplotlib.pyplot as plt
# import easygui
import sys
import os


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


if __name__ == "__main__":
    # file = easygui.fileopenbox(default='F:/huangchunhua/python_item/2023-03-08_143802.log')
    # print(file)
    x_real, y_real = parse_real_path("level.log")
    x_plan, y_plan = parse_planing_path("level.log")
    # print("wheelspeed shape: ", wheelspeed.shape)

    plt.plot(x_plan, y_plan, 'r.-', label="planing path")
    plt.plot(x_real, y_real, 'c', label="real path")

    plt.legend()
    # plt.xlim(0, 5)
    # plt.ylim(-10, 10)
    plt.xlabel("x(m)")
    plt.ylabel('y(m)')
    plt.title("planing real path compare")
    plt.show()
