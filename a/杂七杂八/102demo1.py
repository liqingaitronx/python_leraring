class persion:
    def __init__(self,age,name):
        self.__age = age
        self.name = name

    def stuy(self):
        print("jinnian",str(self.__age),"sui")

james  = persion(30,"zhans")

james.stuy()


print(dir(james))
