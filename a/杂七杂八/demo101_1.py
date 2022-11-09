class Amimal(object):
    def eat(self):
        print("1")

class dog(Amimal):
    def eat(self):
        print("2")

class cat(Amimal):
    def eat(self):
        print("3")
class persion(Amimal):
    def eat(self):
        print(1111)
def A(Aminal):
    Aminal.eat()

A(persion())
A(cat())
A(dog())