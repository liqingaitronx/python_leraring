class fa:
    pass

class ma:
    pass

class fam:
    def __init__(self,fa,ma):
        self.fa = fa
        self.ma = ma

#变量的赋值
fa1 = fa()
fa2 = fa1
print(fa1,fa2)

print("-----")
mo1 = ma()
fam = fam(fa1,fa2)


import copy

fam2 = copy.copy(fam)
print(fam,fam.ma,fam.fa)
print(fam2,fam2.ma,fam2.fa)


#深拷贝
fam3 = copy.deepcopy(fam)
