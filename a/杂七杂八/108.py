class sty(object):
    def __new__(cls, *args, **kwargs):
        print("new方法被调用,id值为{0}".format(id(cls)))
        obj = object.__new__(cls)
        print("obj对象创建出来后，ID值为{0}".format(id(obj)))
        return obj

    def __init__(self,name,age):
        self.name = name
        self.age = age


obj = sty("james",18)
print("obj对象的id值{0}".format(id(obj)))