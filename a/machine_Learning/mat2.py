import matplotlib.pyplot as plt
import numpy
# x = numpy.array([3,8,10,11])
# y = numpy.array([4,3,4,3])
# plt.plot(x,color = 'g')
# plt.plot(y,marker= 'o',color = 'r')
# plt.show()
#------------------------------------------
z = numpy.array([0,1,2,3])
z1 = numpy.array([3,8,1,10])
z3  = numpy.array([4,5,6,7])
z4  = numpy.array([6,2,6,11])
plt.plot(z,z1,z3,z4)
plt.title("Sports Watch Data", loc = 'left')
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()
