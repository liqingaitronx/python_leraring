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
plt.show()