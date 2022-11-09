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


stu1 = student("JAME",20)
STU2 = student("aa",20)
stu1.address = "changsha"
print(stu1.age, stu1.address, stu1.name)

def play():
    print("外面的叫函数")
stu1.play = play()
stu1.play
STU2.play = play()
STU2.play