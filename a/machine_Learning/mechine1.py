import scipy.stats as ss
#平均值、中位数和众数
import numpy
sp = [80,99,100,90,99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(sp)  # mean 求平均数
print(x)
y = numpy.median(sp)#median求中位数
print(y)#中位数

z = ss.mode(sp) #scipy.stats
print(z)  #求出现最多次数

st = numpy.std(sp)
print(st)# 求标准差σ

var = numpy.var(sp)
print([var]) #求方差σ2

