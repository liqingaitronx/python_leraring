import numpy as np
import matplotlib.pyplot as plt

import sys
import os

def parse_vehraw(filename):
    alldata = []
    times = []
    with open(filename, 'r') as f:
        for line in f:
            pos = line.find("vehraw")
            if pos == -1:
                continue
            line = line[1:]
            pos = line.find(">")
            if pos == -1:
                print("bad input line: {}".format(line))
                continue
            times.append(int(line[:pos]))
            pos = line.find("wheel_edge")
            if pos == -1:
                print("missing wheel_ege: {}".format(line))
                continue
            datastr = line[pos+12:]
            pos = datastr.find(";")
            if pos == -1:
                print("missing semicolon: {}".format(datastr))
                continue
            datastr = datastr[:pos]
            rec = datastr.split(',')
            if 4 != len(rec):
                print("incomplete wheel_edge: {}".format(rec))
                continue
            data = [int(d) for d in rec]
            alldata.append(data)
    return np.asarray(times), np.asarray(alldata)

if __name__ == "__main__":
    times, wheelspeed = parse_vehraw("canbus_rec.txt")
    print("wheelspeed shape: ", wheelspeed.shape)

    fig, ax = plt.subplots()
    ax.plot(times, wheelspeed[:, 0], 'm.-', label = "front left")
    ax.plot(times, wheelspeed[:, 1], 'r.-', label = "front right")
    ax.plot(times, wheelspeed[:, 2], 'b.-', label = 'rear left')
    ax.plot(times, wheelspeed[:, 3], 'k.-', label = 'rear right')
    ax.legend()
    ax.set_xlabel("time(ms)")
    ax.set_ylabel('wheel speed sensor reading')
    ax.set_title("wheel_edges data")
    plt.show()

"""<412259><9456>vehraw: steering:7979.0;speed:0.0;wheel_speed:0.0,0.0,0.0,0.0;wheel_edges:1123,1431,711,1185;accel:0.0,0.0,0.0,0.0;
    <412268><9462>gear:D"""