import matplotlib.pyplot as plt
substr1 = "PurePursuitTrajectoryC current position","PurePursuitTrajectoryC target point position"
substr2 = "GetControlValueSrc"
x_list, y_list, heading_angle_list, steering_angle_list,nearest_index_list,velocity_list,gear_list,target_x_list,target_y_list,target_index_list = \
    [[] for i in range(10)]
testlist=open(r'C:\Users\EDY\Desktop\python\a\dlt_txt\logfile.txt','r')

def func(testlist):
    for line in testlist:
        if substr1[0] in line:
            x_list.append(float(line[line.index("(") + 1:line.index(",") + 0]))
            y_list.append(float(line[line.index(", ") + 1:line.index(")") + 0]))
            heading_angle_list.append(float(line[line.index("angle: ") + 7:line.index(", steering") + 0]))
            steering_angle_list.append(float(line[line.index("steering angle:") + 15:line.index(", path") + 0]))
            nearest_index_list.append(float(line[line.index("path index: ") + 12:line.index(", velocity") + 0]))
            velocity_list.append(float(line[line.index("velocity: ") + 10:line.index(", gear") + 0]))
            gear_list.append(float(line[line.index("gear: ") + 6]))

        if substr1[1] in line:
            target_x_list.append(float(line[line.index("(") + 1:line.index(",") + 0]))
            target_y_list.append(float(line[line.index(", ") + 1:line.index(")") + 0]))
            target_index_list.append(float(line[line.index(" path index: ") + 13:].replace("\n","")))
    return x_list,y_list,heading_angle_list,steering_angle_list,nearest_index_list,velocity_list,gear_list,target_x_list,target_y_list,target_index_list

#获取第一次下发的期望车速值
def func1(testlsit,substr2):
    maxVel =[]
    for line in testlsit:
        if substr2 in line:
            maxVel.append(float(line[line.index("ValueSrc ") + 8:line.index(",") + 0]))
            break
    return maxVel

#获取实际车速达到期望车速值
def func2(func1,velocity_list):
    for vas in velocity_list:
        if  func1[0] <= vas:
            print(vas)

# func2(func1(testlist,substr2),func(testlist)[5])
# plt.figure(1)
# plt.plot(float(x_list), float(y_list))
time = [x*0.01 for x in range(0, len(func(testlist)[0]))]
plt.figure(2)
plt.plot(time, heading_angle_list)
plt.xlabel("time(s)")
plt.ylabel("heading angle(rad)")
plt.figure(3)
plt.plot(time, steering_angle_list)
plt.xlabel("time(s)"),plt.ylabel("steering angle(rad)")
plt.figure(4)
plt.plot(time, velocity_list)
plt.xlabel("time(s)")
plt.ylabel("velocity(m/s)")
plt.figure(5)
plt.plot(time, gear_list)
plt.xlabel("time(s)"),plt.ylabel("gear")
plt.show()