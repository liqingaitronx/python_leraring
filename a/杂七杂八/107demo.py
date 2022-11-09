class persion(object):
    def __init__(self,name, adress):
        self.name = name
        self.adress = adress

    def __str__(self):
        return  "{0},{1}".format(self.name ,self.adress)


stu = persion("123","2424")
print(str(stu))

