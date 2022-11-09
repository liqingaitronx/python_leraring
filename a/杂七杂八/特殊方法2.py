class persion(object):
    def __init__(self,name):
        self.name = name
    def __add__(self, other):
        return self.name+other.name # 让对象相加的方法

    def __len__(self): #让对象可以计算长度
        return len(self.name)


s1 = persion("lisi")
s2 = persion("zhangsan")
ss = s1.__add__(s2) # 类似于 s1+s2
print(s2+s1)# 对象相加
print(ss)

print("-----------")

list = [1,2,3,4,5,6]
print(list.__len__())

print(len(s1)) # 调用类里面的对象