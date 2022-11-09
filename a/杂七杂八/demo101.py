import traceback
"""
try:
    a = int(input("请输入一个数字"))
    b = int(input("请输入另一个数字"))
    result = a / b
    print(result)

except:
    print("输入的字符为0或不是数字")
"""

class student:
    name = "lisi"
    age = 19


    def eat(self):
        print("能吃三碗饭")

    def calc(self):
        print(100*100)

    @staticmethod
    def me():
        print("静态类对象")

    @classmethod
    def ls(cls):
        print("DONGTAI")

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = student("张三", 18)
print(stu)
print(type(stu))
print(id(stu))
print("----------------LEIDUIXIANG")
print(student)
print(type(student))
print(id(student))
# bbc = stu.me()
# print(bbc)
print("---------")


student.eat(stu)