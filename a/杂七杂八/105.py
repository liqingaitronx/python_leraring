class persion(object):
    def __init__(self,name ,age):
        self.name = name
        self.age = age


    def info(self):
        print(self.name, self.age)

class Student(persion):
    def __init__(self,name,age,ag):
        super().__init__(name,age)
        self.ag = ag

class teacher(persion):
    def __init__(self, age, name, adress):
        super().__init__(age, name)
        self.adress = adress

stu = Student(30,"James", 000 )

stu.info()
