<<<<<<< HEAD
import  matplotlib.pyplot as plt
import numpy as np
# 显示多个绘图
#plot1
x = np.array([0,1,2,3])
y = np.array([2,3,4,5])

plt.subplot(2,2,1)
plt.plot(x,y)

#plot2
x = np.array([2,3,4,5])
y = np.array([10,20,30,40])

plt.subplot(2,2,2)
plt.plot(x,y)
plt.show()


x = np.array([2,3,4,5])
y = np.array([10,20,30,50])

plt.subplot(2,2,3)
plt.plot(x,y)
=======
import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, color='red')#如果需不同颜色则后面加color
#散点图显示
>>>>>>> 74a3865a5ece24f901b44a5b25fb058f10e09501
plt.show()