class A():
    pass
class B():
    pass
class C(A,B):
    def __init__(self, name, ad):
        self.name = name
        self.ad = ad

stu = C("jame","16")
print(stu.__dict__)
print(B.__eq__)



